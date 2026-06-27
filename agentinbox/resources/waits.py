from __future__ import annotations

from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import AgentInboxClient


class Wait:
    """Represents a wait."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.object = data.get("object")
        self.inbox_id = data.get("inboxId")
        self.message_id = data.get("messageId")
        self.type = data.get("type")
        self.status = data.get("status")
        self.timeout_seconds = data.get("timeoutSeconds")
        self.filters = data.get("filters")
        self.expires_at = data.get("expiresAt")
        self.result = data.get("result")
        self.created_at = data.get("createdAt")
        self.completed_at = data.get("completedAt")

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
        """List waits for an inbox via session details is not supported by the public API."""
        raise NotImplementedError("The public API does not expose /inboxes/{id}/waits")
