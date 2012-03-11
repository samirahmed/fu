from __future__ import with_statement

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
import os
import shutil

package = ['lib']
SCRIPT_TO_INSTALL = 'src/fu'
SCRIPT_TO_RENAME = 'src/fu.py'

if os.path.exists(SCRIPT_TO_INSTALL):
  # Read size is 128*20 for no good reason.
  # Just want to avoid reading in the whole file, and read in a multiple of 128.
  # Shamelessly stole this function from googlecl/docs/base.py
  def _md5_hash_file(path, read_size=2560):
    """Return a binary md5 checksum of file at path."""
    import hashlib
    hash_function = hashlib.md5()
    with open(path, 'r') as my_file:
      data = my_file.read(read_size)
      while data:
        hash_function.update(data)
        data = my_file.read(read_size)
    return hash_function.digest()
  # If running from trunk, SCRIPT_TO_RENAME should exist.
  # For the distributed tarball, they should not.
  if os.path.exists(SCRIPT_TO_RENAME) and\
     not _md5_hash_file(SCRIPT_TO_INSTALL) == _md5_hash_file(SCRIPT_TO_RENAME):
    print SCRIPT_TO_INSTALL + ' exists and is not the same as ' +\
          SCRIPT_TO_RENAME
    print 'Not trusting ' + SCRIPT_TO_INSTALL
    print 'Please update it or remove it.'
    exit(-1)
else:
  shutil.copy(SCRIPT_TO_RENAME, SCRIPT_TO_INSTALL)

setup(
    name="fu",
    version="0.1.1",
    description="Commandline Interface for commandlinefu.com",
    author="Samir Ahmed",
    author_email="samir@samir-ahmed.com",
    url="http://github.com/samirahmed/fu",
    packages=package,
 		package_dir={'lib':'src/lib'},
 		scripts = [SCRIPT_TO_INSTALL]
	)
