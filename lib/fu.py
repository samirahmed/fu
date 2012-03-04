#!/usr/bin/python

import os
import json
import urllib2
import sys
import base64
import time
import argparse
from  terminalColor import color

# Start time
start = int(round(time.time() * 1000))

def parse():

		# Create an argument parser for use dealing with the various command line arguments
		descriptionStr = "%s is a command line iterface for the commandlinefu.com. You can use cfu to tap into the conventional CLI wisdom of the internet " %(color.cyan("cfu"))

		parser = argparse.ArgumentParser( prog = "cfu", description = descriptionStr, add_help = True)
#		parser.add_argument("-i","--Interactive", dest ="interactive", action = "store_true" , default = False, help = "Interacive mode enables you to run a command" );
		parser.add_argument("-c","--count", action="store" ,dest = "count" , default = 3, type = int , help = " The number of search results to display, default is 3");
		parser.add_argument("-a","--all",dest = "showAll",  action = "store_true", default = False, help = "Display all the search results" )
		parser.add_argument("-v", "--verbose",dest = "verbose", action = "store_true", default = False, help = "Show vote counts and url")
		parser.add_argument("query_terms" , nargs=argparse.REMAINDER)

		return parser.parse_args();


def api( query_terms ) :
		query = " ".join(query_terms)										# Create query from commandline args
		
		query_b64 = base64.b64encode(query ) 						# Get the base 64 encoded query

		url =  "http://www.commandlinefu.com/commands/matching/" + query + "/" + query_b64 + "/json/"
		url = url.replace(" ","%20")										# Generate the url

		try :																						#	Make request to the commandline fu API, split response by lines and print
					results  				= urllib2.urlopen(url)
					response_text	 	= results.read()
					return json.loads(response_text)					# Create json file and return

		except urllib2.URLError, e:
				sys.exit("cfU: ERROR. Unable to connect to commandlinefu.com") 

def display ( response_json , isVerbose, count , showAll ) :

		total = len(response_json)
		# Check if we have any results, if inform user and exit
		
		if ( total  <1 ) :
				print "\tcfu: No Results Matching Query"
				sys.exit(0)
		
		display_count = total if showAll else min(total,count)

		num = 1

		# Print each response
		for result in response_json[: display_count]:
				print ' %d\t# ' % num , result['summary']
				print '\t', result['command']
				if isVerbose :
						print '\tURL: ' , result['url']
						print '\tvotes: ', result['votes'] 
				print ""
				num += 1

		# Print the duration and number of responses
		duration =  int(round(time.time() * 1000)) -  start 
		print "\t%dms total:%d" % ( duration, total )		

		return display_count
#
#def interact( response_json , length) :
#		
#		# Prompt user for which commaind they wish to run
#		index_string = raw_input("\tRun Command (1-%d):" % length )
#		index = int(index_string)
#
#		# Check if index valid and if so run
#		if index <= length and index > 0 :	
#				os.system(response_json[index-1]['command'].encode('ascii','ignore'))
#				print response_json[index-1]['command'] , type( response_json[index-1]['command'].encode('ascii','ignore'))
#		sys.exit(0)
#		

def main() : 

		args = parse()																															# parse the commandline input
		
		response_json =  api( args.query_terms)																			# get json from api
		
		count =	display( response_json, args.verbose, args.count , args.showAll ) 	# print results

#		if args.interactive :
#				interact(response_json, count)																					 prompt user for which command to run
#
if __name__ == "__main__":
		
		if len(sys.argv) == 1 :
				print "%s: Incorrect usage, please include search terms. See 'cfu --help' " % ( color.cyan("cfu") ) 
		else :
				main( )
