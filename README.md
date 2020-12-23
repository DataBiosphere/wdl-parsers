# wdl-parsers

A Python package that provides the generated `Hermes` and `Antlr4` WDL parsers for Python.

| Version | Parser(s) | Module |
|---------|-----------|--------|
| draft-2 | Hermes | draft2 |
| v1.0 | Antlr4 | v1 |
| development | Antlr4 |dev |


## Installation

From the CLI:

```
pip install wdlparse
```

## Usage

```python
# the following modules are available:
import wdlparse.draft2
import wdlparse.v1
import wdlparse.dev
```

```python
# draft-2 hermes parser
from wdlparse.draft2 import wdl_parser

# 1.0 antlr4 parser
from wdlparse.v1 import (
    WdlV1Lexer,
    WdlV1Parser
)

# development antlr4 parser
from wdlparse.dev import (
    WdlLexer,
    WdlParser
)

# parse WDL files with these parsers
# ...
```

## License

The grammar and generated files come from [openwdl/wdl](https://github.com/openwdl/wdl/) under the [BSD 3-Clause "New" or "Revised" License](https://github.com/openwdl/wdl/blob/main/LICENSE).
