from setuptools import setup, find_packages

install_requires = [
      "antlr4-python3-runtime==4.8",
]

dev_requires = [
      "hermes-parser==2.0rc6",
]

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()


setup(name='wdl_parsers',
      version='0.2.0',
      description='WDL parsers for Python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/DataBiosphere/wdl-parsers',
      author='William Gao',
      author_email='wlgao@ucsc.edu',
      license="Apache License v2.0",
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      install_requires=install_requires,
      extras_require={'dev': dev_requires})
