# Project Context: LangGraph AI Model

## Overview
{{ONE_LINE_DESCRIPTION_OF_LANGGRAPH_APP}}

## Purpose
{{WHAT_AI_TASK_DOES_THIS_AGENT_PERFORM}}

## Tech Stack
- **Language:** Python {{VERSION}}
- **Framework:** LangGraph {{VERSION}}, LangChain {{VERSION}}
- **LLM Provider:** {{OPENAI/ANTHROPIC/OTHER}} ({{MODEL_NAME}})
- **Package Manager:** uv
- **State Management:** {{TypedDict / Pydantic / CustomState}}
- **Persistence:** {{MemorySaver / SqliteSaver / PostgresSaver / None}}

## LangGraph Architecture
### State Schema
```python
class {{StateName}}(TypedDict):
    {{field_name: type}}: {{description}}
    {{field_name: type}}: {{description}}
```

### Nodes
| Node Name | Purpose | LLM Used? | Tools Used? |
|-----------|---------|-----------|-------------|
| {{node_1}} | {{description}} | {{Yes/No}} | {{tool_list}} |
| {{node_2}} | {{description}} | {{Yes/No}} | {{tool_list}} |

### Edges
| From | To | Type | Condition (if conditional) |
|------|----|------|---------------------------|
| {{START}} | {{node_1}} | Normal | N/A |
| {{node_1}} | {{node_2}} | Conditional | {{condition_function}} |
| {{node_2}} | {{END}} | Normal | N/A |

## Entry Point
```bash
uv run {{PROJECT_NAME}}
# or
python -m {{PACKAGE_NAME}}.main
```

## Environment Variables
| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| {{API_KEY_NAME}} | {{LLM provider API key}} | Yes | sk-... |
| {{LANGCHAIN_API_KEY}} | LangSmith tracing (optional) | No | ls-... |

## How to Run
```bash
# Install dependencies
uv sync

# Run the agent
uv run {{PROJECT_NAME}}

# Run with LangSmith tracing
LANGCHAIN_TRACING_V2=true uv run {{PROJECT_NAME}}
```

## Key Design Decisions
- {{Why this state structure?}}
- {{Why this node/edge pattern?}}
- {{Why this checkpointer?}}

## Known Limitations
- {{Limitation_1}}
- {{Limitation_2}}

## Next Steps / TODOs
- [ ] {{Add human-in-the-loop interrupt}}
- [ ] {{Add streaming output}}
- [ ] {{Add more tools}}
