from typing import Any, Dict

from .client import AgentTempClient


class Extraction:
    """Represents an extraction."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.message_id = data.get("message_id")
        self.inbox_id = data.get("inbox_id")
        self.type = data.get("type")
        self.value = data.get("value")
        self.url = data.get("url")
        self.confidence = data.get("confidence")
        self.candidates = data.get("candidates", [])
        self.created_at = data.get("created_at")

    def __repr__(self) -> str:
        return f"Extraction(id={self.id}, type={self.type})"


class ExtractionsResource:
    """Extraction operations."""

    def __init__(self, client: AgentTempClient):
        self._client = client

    def list(self, inbox_id: str) -> list:
        """List extractions for an inbox."""
        return self._client.get(f"/inboxes/{inbox_id}/extractions")
