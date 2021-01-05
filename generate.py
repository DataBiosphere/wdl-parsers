# Copyright (C) 2021 Regents of the University of California
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import logging
import sys

from utils import (
    check_java,
    check_antlr,
    check_hermes,
    run_antlr,
    run_hermes,
    download_antlr,
    download_grammar_from_github,
)

"""
Generator script for the WDL parsers.
"""

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.setLevel(logging.DEBUG)


def generate_dev():
    """
    Generate parsers for the development version.
    """
    if not check_java():
        logger.warning('Failed to generate parsers for development.  Java is not installed.')
        return False

    if not check_antlr():
        download_antlr()

    # download grammar if it doesn't exist already
    download_grammar_from_github('versions/development/parsers/antlr4/WdlLexer.g4', 'WdlLexer.g4')
    download_grammar_from_github('versions/development/parsers/antlr4/WdlParser.g4', 'WdlParser.g4')

    run_antlr(['-o', 'wdlparse/dev', 'WdlLexer.g4'])
    run_antlr(['-listener', '-visitor', '-o', 'wdlparse/dev', 'WdlParser.g4'])


def generate_v1():
    """
    Generate parsers for the 1.0 version.
    """
    if not check_java():
        logger.warning('Failed to generate parsers for 1.0.  Java is not installed.')
        return False

    if not check_antlr():
        download_antlr()

    # download grammar if it doesn't exist already
    download_grammar_from_github('versions/1.0/parsers/antlr4/WdlV1Lexer.g4', 'WdlV1Lexer.g4')
    download_grammar_from_github('versions/1.0/parsers/antlr4/WdlV1Parser.g4', 'WdlV1Parser.g4')

    run_antlr(['-o', 'wdlparse/v1', 'WdlV1Lexer.g4'])
    run_antlr(['-listener', '-visitor', '-o', 'wdlparse/v1', 'WdlV1Parser.g4'])


def generate_draft2():
    """
    Generate parsers for the draft-2 version.
    """
    if not check_hermes():
        logger.warning('Failed to generate parsers for draft-2.  Hermes is not installed.')
        logger.warning('Install hermes-parser via `pip install hermes-parser`.')
        return False

    # download grammar if it doesn't exist already
    download_grammar_from_github('versions/draft-2/parsers/grammar.hgr', 'grammar.hgr')

    run_hermes('grammar.hgr', 'wdlparse/draft2')


def main(args=None):
    parser = argparse.ArgumentParser(description='WDL parsers generation script.')
    parser.add_argument('-v', '--version',
                        nargs='*',
                        choices=('all', 'draft-2', '1.0', 'development', ),
                        default=['all'],
                        help='version(s) to generate.')

    args = parser.parse_args(args)
    versions = set(args.version)

    if 'all' in versions:
        logger.info(f'Generating parsers for all versions.')
        generate_draft2()
        generate_v1()
        generate_dev()
        return

    for v in versions:
        logger.info(f'Generating parsers for: {v}.')
        if v == 'draft-2':
            generate_draft2()
        elif v == '1.0':
            generate_v1()
        elif v == 'development':
            generate_dev()


if __name__ == '__main__':
    main()
