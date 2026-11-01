# Project Context: {{PROJECT_NAME}}

## Overview
{{ONE_LINE_DESCRIPTION}}

## Purpose
{{WHY_THIS_PROJECT_EXISTS}}

## Tech Stack
- **Language:** Python {{VERSION}}
- **Package Manager:** uv
- **Key Dependencies:** {{DEPENDENCY_LIST}}
- **Entry Point:** {{ENTRY_POINT_COMMAND}}

## Project Structure
```
{{PROJECT_ROOT}}/
├── pyproject.toml          # Project config & dependencies
├── .env                    # Environment variables (gitignored)
├── .gitignore              # Git ignore rules
├── src/
│   └── {{PACKAGE_NAME}}/
│       └── main.py         # Application entry point
└── {{OTHER_KEY_FILES}}
```

## Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| {{VAR_NAME}} | {{DESCRIPTION}} | {{Yes/No}} | {{DEFAULT}} |
| {{VAR_NAME}} | {{DESCRIPTION}} | {{Yes/No}} | {{DEFAULT}} |

## How to Run
```bash
# Install dependencies
uv sync

# Run the application
uv run {{PROJECT_NAME}}

# Or run directly
python src/{{PACKAGE_NAME}}/main.py
```

## Key Design Decisions
- {{DECISION_1}}
- {{DECISION_2}}

## Known Limitations
- {{LIMITATION_1}}
- {{LIMITATION_2}}

## Next Steps / TODOs
- [ ] {{TODO_ITEM_1}}
- [ ] {{TODO_ITEM_2}}
