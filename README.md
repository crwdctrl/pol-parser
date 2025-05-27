# pol-parser

A Python tool to parse and display contents of Windows Group Policy `.pol` files (like `Registry.pol`), commonly used in Group Policy Objects (GPOs).

## Features

- Parses `.pol` files in PReg format  
- Extracts registry key paths, value names, types, and data
- Supports common registry value types like `REG_SZ`, `REG_DWORD`, `REG_BINARY`, etc. 
- Handles unknown types and corrupted entries gracefully  
- CLI interface for quick terminal use  

## Installation

Clone the repository and install it locally:

```bash
git clone https://github.com/crwdctrl/pol-parser.git
cd pol-parser
pip install .
```
## Usage

### CLI
```bash
python -m polparser.cli /path/to/Registry.pol
```

### As a module
```bash
from polparser.parser import parse_pol

with open("/path/to/Registry.pol", "rb") as f:
    data = f.read()

results = parse_pol(data)
print(results[:3])  # Display first few parsed entries
```

## Output format

```bash
Key                                                      Value Name                    Type         Value
================================================================================================================
Software\Policies\...                                    ExampleValue                  REG_SZ       SomeValue
...
```

## Testing

Run tests with:

```bash
pytest tests/
```

## Requirements

Python 3.6+
