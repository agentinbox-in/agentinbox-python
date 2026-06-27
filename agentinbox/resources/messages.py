from __future__ import annotations

from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import AgentInboxClient


class Message:
    """Represents a message."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.object = data.get("object")
        self.inbox_id = data.get("inboxId")
        self.from_email = data.get("fromEmail")
        self.from_name = data.get("fromName")
        self.to_email = data.get("toEmail")
        self.subject = data.get("subject")
        self.has_attachments = data.get("hasAttachments")
        self.size_bytes = data.get("sizeBytes")
        self.text_body = data.get("textBody")
        self.html_body = data.get("htmlBody")
        self.received_at = data.get("receivedAt")

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
