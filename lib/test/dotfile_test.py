
"""
Test Script for dotfile config module
"""

import os
import sys
import json
# Add to sys.path and then import
sys.path.insert(0, os.path.abspath(".."))
from config import dotfile


samplefile = open('sample.json','r')
sample = samplefile.read()
samplefile.close()

def add_response( string ):
		# Add the sample response to the dot file
		dfile = dotfile()
		dfile.save_result(string)
		dfile.save()
		print "Wrote Sample JSON to dotfile"


def create():

		filepath =os.path.join(os.getenv('HOME'),'.fu')
		
		# Put some crap in the file
		os.remove(filepath)

		# Create a dot file test
		dfile = dotfile()
		exists = os.path.isfile(filepath)
		print "File Exists? "	+ str(exists)
		dfile.save()

def read_results( original):
		#	 Read from the dotfile and see if the sample json is there
		dfile = dotfile()
		saved = dfile.result()
		dfile.save()
		if saved == original:
				print "File Read is same as original!"
		else :
				print "Oops! File Read is not the samea as the original"
				print "Original : " + str( type(original) )
				print original
				print "================================================="
				print "Saved : " + str( type( saved ))
				print saved

def add_command( ):
		# Load the dotfile, get the command
		dfile = dotfile()
		saved = dfile.result()
		command = json.loads(saved)[0]['command']
		dfile.save_copy(command)
		print "Saving copy command"
		dfile.save()

		return command


def read_command( string ):
		
		# Load the dotfile, get the command
		dfile = dotfile()
		command = dfile.last()
		dfile.save()

		if command  == string :
				print "Command Saved and Loaded Successfully? Yes"
		else :
				print "Oops! Copied command was not the same!"

def read_history(command):
		
		# Read history from dot file
		dfile = dotfile()
		history = dfile.history()[0]
		if history == command :
				print "History Save Loaded Succesful? True" 
		else:
				print "History Save Loaded Succesful? False" 

print "\nDotfile Tests --------------------------\n"

# Test creating a dotfile
create()

# Test Adding and removing json string results from a dotfile
add_response(sample)
read_results(sample)

# Test Adding and removing last copied commands to the dotfile
command = add_command()
read_command(command)

# Test Saving and loading history to the dotfile
read_history(command)

