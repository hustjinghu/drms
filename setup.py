#!/usr/bin/env python
import os, re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


NAME = 'drms_json'
DESCRIPTION = 'Access to HMI, MDI and AIA data products from the JSOC database.'
LONG_DESCRIPTION = open('README.md').read()
AUTHOR = 'Kolja Glogowski'
AUTHOR_EMAIL = '"Kolja Glogowski" <kolja@pixie.de>'
URL = 'https://github.com/kbg/drms_json'
LICENSE = 'MIT'

# Read version string from drms_json.py without importing the module to
# prevent an import error in case numpy, pandas or six are not installed yet.
m = re.search(r"""^\s*__version__\s*=\s*["'](.+)["']\s*$""",
              open('drms_json.py').read(), re.MULTILINE)
VERSION = m.group(1)

# For distutils builds: Make sure the MANIFEST file ist generated from
# MANIFEST.in by removing the old file.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      py_modules=['drms_json'],
      install_requires=['numpy>=1.9.0', 'pandas>=0.14.1', 'six>=1.8.0'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Astronomy'],
      )
