from typing import Any, Dict, List, Optional

from .client import AgentInboxClient


class Inbox:
    """Represents an inbox."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.email_address = data.get("email_address")
        self.local_part = data.get("local_part")
        self.domain_id = data.get("domain_id")
        self.ttl_seconds = data.get("ttl_seconds")
        self.expires_at = data.get("expires_at")
        self.status = data.get("status")
        self.purpose = data.get("purpose")
        self.created_at = data.get("created_at")
        self.completed_at = data.get("completed_at")
        self.session_id = data.get("session_id")

    def __repr__(self) -> str:
        return f"Inbox(id={self.id}, email={self.email_address})"


class InboxesResource:
    """Inbox operations."""

    def __init__(self, client: AgentInboxClient):
        self._client = client

    def create(
        self,
        ttl_seconds: Optional[int] = None,
        purpose: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> Inbox:
        """Create a new inbox."""
        payload = {}
        if ttl_seconds is not None:
            payload["ttlSeconds"] = ttl_seconds
        if purpose is not None:
            payload["purpose"] = purpose
        if session_id is not None:
            payload["sessionId"] = session_id

        data = self._client.post("/inboxes", json_data=payload)
        return Inbox(data)

    def list(self, limit: int = 50) -> List[Inbox]:
        """List all inboxes."""
        data = self._client.get("/inboxes", params={"limit": limit})
        return [Inbox(item) for item in data.get("data", [])]

    def get(self, inbox_id: str) -> Inbox:
        """Get an inbox by ID."""
        data = self._client.get(f"/inboxes/{inbox_id}")
        return Inbox(data)

    def delete(self, inbox_id: str) -> None:
        """Delete an inbox."""
        self._client.delete(f"/inboxes/{inbox_id}")

    def list_messages(self, inbox_id: str) -> List[Dict[str, Any]]:
        """List messages in an inbox."""
        return self._client.get(f"/inboxes/{inbox_id}/messages")

    def list_extractions(self, inbox_id: str) -> List[Dict[str, Any]]:
        """List extractions in an inbox."""
        return self._client.get(f"/inboxes/{inbox_id}/extractions")
