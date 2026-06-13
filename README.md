# AgentTemp Python SDK

Python SDK for the AgentTemp email verification API.

## Installation

```bash
pip install agenttemp
```

## Quick Start

```python
from agenttemp import AgentTempClient

client = AgentTempClient(api_key="at_live_...")

# Create an inbox
inbox = client.inboxes.create(ttl_seconds=3600, purpose="Signup test")
print(inbox.email_address)

# Wait for OTP
wait = client.waits.create(
    inbox_id=inbox.id,
    type="otp",
    timeout_seconds=120
)
print(wait.result.value)  # "123456"
```

## Features

- Full Python 3.8+ support
- Type hints throughout
- Automatic retry with exponential backoff
- Custom error classes for each API error
- Resource-based API (inboxes, waits, messages, sessions)

## Error Handling

```python
from agenttemp.errors import QuotaExceededError, RateLimitError

try:
    client.inboxes.create()
except QuotaExceededError as e:
    print(f"Quota exceeded: {e.limit}")
except RateLimitError as e:
    print(f"Rate limited, retry after: {e.retry_after}")
```

## Resources

- [API Documentation](https://agentinbox.in/api/v1/openapi.json)
- [Node.js SDK](https://github.com/kunalgawade19042002-gif/agenttemp-node)
- [MCP Server](https://github.com/kunalgawade19042002-gif/agenttemp-mcp)

## License

MIT
