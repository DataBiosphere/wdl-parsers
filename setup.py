from setuptools import setup, find_packages

install_requires = [
      "antlr4-python3-runtime==4.8",
]

dev_requires = [
      "hermes-parser==2.0rc6",
]

setup(name='wdlparse',
      version='0.1.0',
      description='WDL parsers for Python.',
      url='https://github.com/DataBiosphere/wdl-parsers',
      author='William Gao',
      author_email='wlgao@ucsc.edu',
      license="Apache License v2.0",
      packages=find_packages('.'),
      install_requires=install_requires,
      extras_require={'dev': dev_requires})
