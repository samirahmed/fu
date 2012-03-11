
"""
Test Script for terminal Color module
"""

import os
import sys

# Add to sys.path and then import
sys.path.insert(0, os.path.abspath(".."))
from terminalColor import color

print "\nColor Test --------------------\n"
# Test all will call all functions
# expect to get a print ouf of different colors
color.testAll('Terminal Color Test')



