import json
import time
from typing import Any, Dict, Optional

import requests

from .errors import (
    AgentTempError,
    InvalidRequestError,
    NotFoundError,
    QuotaExceededError,
    RateLimitError,
    UnauthorizedError,
)
from .resources.extractions import ExtractionsResource
from .resources.inboxes import InboxesResource
from .resources.messages import MessagesResource
from .resources.sessions import SessionsResource
from .resources.waits import WaitsResource


class AgentTempClient:
    """Client for the AgentTemp API."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://tempmailai.vercel.app/api/v1",
        timeout: int = 30,
        retries: int = 3,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        })

        # Resources
        self.inboxes = InboxesResource(self)
        self.waits = WaitsResource(self)
        self.messages = MessagesResource(self)
        self.extractions = ExtractionsResource(self)
        self.sessions = SessionsResource(self)

    def _request(
        self,
        method: str,
        path: str,
        json_data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make an API request with retries."""
        url = f"{self.base_url}{path}"
        last_error = None

        for attempt in range(self.retries):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    json=json_data,
                    params=params,
                    timeout=self.timeout,
                )

                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 1))
                    if attempt < self.retries - 1:
                        time.sleep(retry_after)
                        continue
                    raise RateLimitError(
                        "Rate limit exceeded", retry_after=retry_after
                    )

                data = response.json() if response.text else {}

                if not response.ok:
                    error = data.get("error", {})
                    code = error.get("code", "unknown")
                    message = error.get("message", "Unknown error")

                    if code == "unauthorized":
                        raise UnauthorizedError(message)
                    elif code == "rate_limited":
                        raise RateLimitError(message)
                    elif code == "quota_exceeded":
                        limit = error.get("limit", 0)
                        raise QuotaExceededError(message, limit=limit)
                    elif code == "not_found":
                        raise NotFoundError(message)
                    elif code == "invalid_request":
                        raise InvalidRequestError(message)
                    else:
                        raise AgentTempError(message, code)

                return data

            except requests.exceptions.RequestException as e:
                last_error = e
                if attempt < self.retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue

        raise AgentTempError(
            f"Request failed after {self.retries} attempts: {last_error}"
        )

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request."""
        return self._request("GET", path, params=params)

    def post(self, path: str, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request."""
        return self._request("POST", path, json_data=json_data)

    def delete(self, path: str) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self._request("DELETE", path)

    def patch(self, path: str, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PATCH request."""
        return self._request("PATCH", path, json_data=json_data)
