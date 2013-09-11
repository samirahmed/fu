
"""
Test Script for commandlinefu api module
"""

import os
import sys

# Add to sys.path and then import
sys.path.insert(0, os.path.abspath(".."))
from api import API

print "\nAPI test ------------------------\n"

api = API( sys.argv[1:] )
api.load()
api.display( True, 3 ,True)
	
