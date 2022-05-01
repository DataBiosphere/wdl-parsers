# wdl-parsers

NOTE: this is a fork of the [`wdl-parsers`](https://github.com/DataBiosphere/wdl-parsers) package.


A Python package that provides the generated `Hermes` and `Antlr4` WDL parsers for Python.

|   Version   | Parser(s) |   Module    |
|-------------|-----------|-------------|
| draft-2     | Hermes    | draft_2     |
| v1.0        | Antlr4    | v1_0        |
| v1.1        | Antlr4    | v1_1        |
| development | Antlr4    | development |


## Installation

From the CLI:

```
pip install wdl_parsers
```

## Usage

```python
# the following modules are available:
import wdl_parsers.draft_2
import wdl_parsers.v1_0
import wdl_parsers.v1_1
import wdl_parsers.development
```

```python
# draft-2 hermes parser
from wdl_parsers.draft_2 import wdl_parser

# 1.0 antlr4 parser
from wdl_parsers.v1_0.WdlV1Lexer import WdlV1Lexer
from wdl_parsers.v1_0.WdlV1Parser import WdlV1Parser

# 1.1 antlr4 parser
from wdl_parsers.v1_1.WdlV1_1Lexer import WdlV1_1Lexer
from wdl_parsers.v1_1.WdlV1_1Parser import WdlV1_1Parser

# development antlr4 parser
from wdl_parsers.development.WdlLexer import WdlLexer
from wdl_parsers.development.WdlParser import WdlParser

# parse WDL files with these parsers
# ...
```

## License

The grammar files come from [openwdl/wdl](https://github.com/openwdl/wdl/) under the [BSD 3-Clause "New" or "Revised" License](https://github.com/openwdl/wdl/blob/main/LICENSE).
