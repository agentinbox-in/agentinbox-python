from typing import Any, Dict, List, Optional

from .client import AgentTempClient


class Session:
    """Represents a session."""

    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.name = data.get("name")
        self.status = data.get("status")
        self.metadata = data.get("metadata")
        self.expires_at = data.get("expires_at")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    def __repr__(self) -> str:
        return f"Session(id={self.id}, name={self.name})"


class SessionsResource:
    """Session operations."""

    def __init__(self, client: AgentTempClient):
        self._client = client

    def create(
        self,
        name: str,
        ttl_seconds: int = 3600,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Session:
        """Create a new session."""
        payload = {
            "name": name,
            "ttlSeconds": ttl_seconds,
        }
        if metadata:
            payload["metadata"] = metadata

        data = self._client.post("/sessions", json_data=payload)
        return Session(data)

    def list(self, limit: int = 50) -> List[Session]:
        """List all sessions."""
        data = self._client.get("/sessions", params={"limit": limit})
        return [Session(item) for item in data.get("data", [])]

    def get(self, session_id: str, include: Optional[List[str]] = None) -> Dict[str, Any]:
        """Get a session with optional related data."""
        params = {}
        if include:
            params["include"] = ",".join(include)
        return self._client.get(f"/sessions/{session_id}", params=params)

    def complete(self, session_id: str) -> Session:
        """Complete a session."""
        data = self._client.post(f"/sessions/{session_id}")
        return Session(data)
