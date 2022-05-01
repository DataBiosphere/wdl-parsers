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
import logging
import os
import shutil
import subprocess
import sys
from typing import Optional
from urllib.request import urlopen

"""
Utility functions for generating the WDL parsers.
"""

ANTLR_JAR = 'antlr-4.8-complete.jar'


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def check_java() -> bool:
    """ Check if Java is installed on the system."""
    return shutil.which('java') is not None


def check_antlr() -> bool:
    """ Check if antlr is available on the system."""
    return os.path.exists(ANTLR_JAR)


def check_hermes() -> bool:
    """ Check if hermes-parser is available on the system."""
    try:
        import hermes
        return True
    except ImportError:
        return False


def download_from_url(url: str, out_filepath: str):
    """
    Download a file from the Internet. Exception will be raised if anything
    goes wrong.

    :param url: url to fetch from.
    :param out_filepath: file name relative to cwd.
    """
    if not os.path.exists(out_filepath):
        logger.info(f'Downloading "{url}" to "{out_filepath}".')
        with urlopen(url) as res, open(out_filepath, 'wb') as f:
            shutil.copyfileobj(res, f)


def download_antlr():
    """ Download the executable Antlr4 jar to the cwd."""
    download_from_url(f'https://www.antlr.org/download/{ANTLR_JAR}', ANTLR_JAR)


def download_grammar_from_github(filename: str, out_filepath: Optional[str] = None):
    """
    Download a raw grammar file directly from Github. This ensures the most up-to-date
    file will be generated.

    :param filename: file name relative to the OpenWDL repository:
                     https://github.com/openwdl/wdl
    :param out_filepath: file name relative to cwd.
    """
    if not out_filepath:
        out_filepath = os.path.basename(filename)

    url = os.path.join('https://raw.githubusercontent.com/openwdl/wdl/main/', filename)
    download_from_url(url, out_filepath)


def run_command(cmd, suppress_output=False):
    """ Run a shell command."""
    logger.info(f'Running command: "{cmd}".')
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout, stderr = process.communicate()
    if not suppress_output:
        logger.info(stdout)
    if stderr:
        logger.warning(stderr)


def run_antlr(args):
    """ Run Antlr4 with arguments."""
    run_command(f'java -jar {ANTLR_JAR} -Dlanguage=Python3 ' + ' '.join(args), suppress_output=True)


def run_hermes(grammar: str, out_dir: str):
    """ Run the hermes parser generator."""
    cmd = f'hermes generate {grammar} --language=python --name=wdl --header --directory {out_dir}'
    run_command(cmd, suppress_output=True)
