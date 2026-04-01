# MCP Tools Usage Guide

> Correct usage of MCP tools in this project.

---

## Context7 MCP

Context7 is used to fetch up-to-date documentation for libraries and frameworks.

### Correct Usage

**Both `libraryName` and `query` are required parameters:**

```python
# Correct: Both parameters provided
mcp__context7__resolve-library-id(
    libraryName="astrbot",
    query="scheduled task timer cron async scheduling"
)

# Wrong: Missing query parameter
mcp__context7__resolve-library-id(libraryName="astrbot")  # ERROR!
```

### Query Tips

The `query` parameter should describe what you're looking for:
- Use keywords related to your task
- Include multiple relevant terms
- Example queries:
  - `"scheduled task timer cron async scheduling"`
  - `"message event filter command handler"`
  - `"plugin config initialization lifecycle"`

### After Resolving Library ID

Use the returned library ID to query documentation:

```python
# First resolve the library ID
libraryId = "/astrbotdevs/astrbot-docs"

# Then query specific topics
mcp__context7__query-docs(
    libraryId=libraryId,
    query="unified_msg_origin group chat send_message"
)
```

---

## Other MCP Tools

(Add other MCP tool usage guides as needed)