import os
import sys

# Add to sys.path and then import
sys.path.insert(0, os.path.abspath(".."))
from platform_utils import system

print "\nPlatform Utility Test --------------\n"
if len(sys.argv) > 1:
		my_system = system()
		if my_system.copy( sys.argv[1] ):
				print "Copied to clipboard : " +  sys.argv[1]
		else :
				print "Oops! Unable too copy!"
				print "Looks like you have a " + my_system.name + ". Please ensure you have " + my_system.copy_command
		my_system.open("http://www.commandlinefu.com")
else :
		print "usage: copy.py <copy term> "

		
