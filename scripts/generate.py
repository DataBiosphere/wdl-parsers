# Copyright (C) 2021-2022 Regents of the University of California
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
import os
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


def generate_development(output_base_url: str, output_dir: str = "development"):
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

    output = os.path.join(output_base_url, output_dir)
    run_antlr(['-o', output, 'WdlLexer.g4'])
    run_antlr(['-listener', '-visitor', '-o', output, 'WdlParser.g4'])


def generate_v1_0(output_base_url: str, output_dir: str = "v1_0"):
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

    output = os.path.join(output_base_url, output_dir)
    run_antlr(['-o', output, 'WdlV1Lexer.g4'])
    run_antlr(['-listener', '-visitor', '-o', output, 'WdlV1Parser.g4'])


def generate_v1_1(output_base_url: str, output_dir: str = "v1_1"):
    """
    Generate parsers for the 1.1 version.
    """
    if not check_java():
        logger.warning('Failed to generate parsers for 1.1.  Java is not installed.')
        return False

    if not check_antlr():
        download_antlr()

    # download grammar if it doesn't exist already
    download_grammar_from_github('versions/1.1/parsers/antlr4/WdlV1_1Lexer.g4', 'WdlV1_1Lexer.g4')
    download_grammar_from_github('versions/1.1/parsers/antlr4/WdlV1_1Parser.g4', 'WdlV1_1Parser.g4')

    output = os.path.join(output_base_url, output_dir)
    run_antlr(['-o', output, 'WdlV1_1Lexer.g4'])
    run_antlr(['-listener', '-visitor', '-o', output, 'WdlV1_1Parser.g4'])


def generate_draft_2(output_base_url: str, output_dir: str = "draft_2"):
    """
    Generate parsers for the draft-2 version.
    """
    if not check_hermes():
        logger.warning('Failed to generate parsers for draft-2.  Hermes is not installed.')
        logger.warning('Install hermes-parser via `pip install hermes-parser`.')
        return False

    # download grammar if it doesn't exist already
    download_grammar_from_github('versions/draft-2/parsers/grammar.hgr', 'grammar.hgr')

    output = os.path.join(output_base_url, output_dir)
    run_hermes('grammar.hgr', output)


def main(args=None):
    parser = argparse.ArgumentParser(description="WDL parsers generation script.")
    parser.add_argument("--versions",
                        nargs="*",
                        choices=("all", "draft-2", "1.0", "1.1", "development", ),
                        default=["all"],
                        help="version(s) to generate.")

    args = parser.parse_args(args)
    versions = set(args.versions)

    base_url = "src/wdl_parsers"

    if "all" in versions:
        logger.info(f"Generating parsers for all versions.")
        generate_draft_2(base_url)
        generate_v1_0(base_url)
        generate_v1_1(base_url)
        generate_development(base_url)
        return

    for v in versions:
        logger.info(f"Generating parsers for: {v}.")
        if v == "draft-2":
            generate_draft_2(base_url)
        elif v == "1.0":
            generate_v1_0(base_url)
        elif v == "1.1":
            generate_v1_1(base_url)
        elif v == "development":
            generate_development(base_url)


if __name__ == "__main__":
    main()
