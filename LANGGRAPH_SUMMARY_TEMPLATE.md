# Summary: {{TITLE}}

**Date:** {{DATE}}  
**Branch:** {{GIT_BRANCH}}  
**LangGraph Version:** {{VERSION}}

## What Changed
- {{CHANGE_1}}
- {{CHANGE_2}}
- {{CHANGE_3}}

## LangGraph-Specific Changes
| Area | Before | After | Impact |
|------|--------|-------|--------|
| State schema | {{old_fields}} | {{new_fields}} | {{impact}} |
| Nodes added/removed | {{list}} | {{list}} | {{impact}} |
| Edges modified | {{old_flow}} | {{new_flow}} | {{impact}} |
| Checkpointer | {{old}} | {{new}} | {{impact}} |
| LLM model | {{old}} | {{new}} | {{impact}} |

## Files Modified
| File | Action | Description |
|------|--------|-------------|
| {{PATH}} | {{Created/Modified/Deleted}} | {{DESCRIPTION}} |
| {{PATH}} | {{Created/Modified/Deleted}} | {{DESCRIPTION}} |

## How to Verify
```bash
{{VERIFICATION_COMMAND}}
```
Expected output: {{EXPECTED_OUTPUT}}

Or test the graph:
```python
from {{PACKAGE_NAME}}.main import {{graph_name}}
result = {{graph_name}}.invoke({{"input": "test message"}})
print(result)
```

## Breaking Changes
{{NONE or DESCRIPTION - e.g., "State schema changed, existing checkpoints incompatible"}}

## Notes / Assumptions
{{Any notes about LLM behavior, tool usage, or graph flow}}
