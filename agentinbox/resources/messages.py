from __future__ import annotations

from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import AgentInboxClient


class Message:
    """Represents a message."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.inbox_id = data.get("inbox_id")
        self.from_email = data.get("from_email")
        self.from_name = data.get("from_name")
        self.subject = data.get("subject")
        self.text_body = data.get("text_body")
        self.html_body = data.get("html_body")
        self.received_at = data.get("received_at")
        self.created_at = data.get("created_at")

    def __repr__(self) -> str:
        return f"Message(id={self.id}, subject={self.subject})"


class MessagesResource:
    """Message operations."""

    def __init__(self, client: AgentInboxClient):
        self._client = client

    def get(self, message_id: str) -> Message:
        """Get a message by ID."""
        data = self._client.get(f"/messages/{message_id}")
        return Message(data)

    def extract(self, message_id: str) -> Dict[str, Any]:
        """Extract data from a message."""
        return self._client.post(f"/messages/{message_id}/extract")
