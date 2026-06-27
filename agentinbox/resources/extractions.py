from __future__ import annotations

from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import AgentInboxClient


class Extraction:
    """Represents an extraction."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.object = data.get("object")
        self.message_id = data.get("messageId")
        self.inbox_id = data.get("inboxId")
        self.type = data.get("type")
        self.value = data.get("value")
        self.url = data.get("url")
        self.confidence = data.get("confidence")
        self.candidates = data.get("candidates", [])
        self.source = data.get("source")
        self.created_at = data.get("createdAt")

    def __repr__(self) -> str:
        return f"Extraction(id={self.id}, type={self.type})"


class ExtractionsResource:
    """Extraction operations."""

    def __init__(self, client: AgentInboxClient):
        self._client = client

    def list(self, inbox_id: str) -> list:
        """List extractions for an inbox."""
        data = self._client.get(f"/inboxes/{inbox_id}/extractions")
        return [Extraction(item) for item in data.get("data", [])]
