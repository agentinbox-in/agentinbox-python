from typing import Any, Dict, Optional

from .client import AgentInboxClient


class Wait:
    """Represents a wait."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.inbox_id = data.get("inbox_id")
        self.type = data.get("type")
        self.status = data.get("status")
        self.timeout_seconds = data.get("timeout_seconds")
        self.expires_at = data.get("expires_at")
        self.result = data.get("result")
        self.created_at = data.get("created_at")
        self.completed_at = data.get("completed_at")

    def __repr__(self) -> str:
        return f"Wait(id={self.id}, type={self.type}, status={self.status})"


class WaitsResource:
    """Wait operations."""

    def __init__(self, client: AgentInboxClient):
        self._client = client

    def create(
        self,
        inbox_id: str,
        type: str = "otp",
        timeout_seconds: int = 60,
        filters: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None,
    ) -> Wait:
        """Create a new wait."""
        payload = {
            "inboxId": inbox_id,
            "type": type,
            "timeoutSeconds": timeout_seconds,
        }
        if filters:
            payload["filters"] = filters
        if session_id:
            payload["sessionId"] = session_id

        data = self._client.post("/waits", json_data=payload)
        return Wait(data)

    def get(self, wait_id: str) -> Wait:
        """Get a wait by ID."""
        data = self._client.get(f"/waits/{wait_id}")
        return Wait(data)

    def cancel(self, wait_id: str) -> Wait:
        """Cancel a pending wait."""
        data = self._client.post(f"/waits/{wait_id}/cancel")
        return Wait(data)

    def list(self, inbox_id: str) -> list:
        """List waits for an inbox."""
        return self._client.get(f"/inboxes/{inbox_id}/waits")
