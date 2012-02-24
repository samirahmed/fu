#!/usr/bin/python

''' 
The CommandLineFu API is documented at
->	http://www.commandlinefu.com/site/api/

Website and API are managed by David Winterbottom.
The API documentation states that all request must be in the following form
http://www.commandlinefu.com/commands/<command-set>/<format>/

This file will use it as follows

-format = json
-command-set = matching/ssh/c3No - Search results for the query 'ssh' (note that the final segment is a base64-encoding of the search query)

Written by Samir Ahmed 2012
'''

import sys
import json
import urllib2
import base64
from terminalColor import color

class API:
		''' A Wrapper Class for the commandlinefu.com API '''
		def __init__(self, query_terms):
				# Store the search terms
				self.search_terms = query_terms

				# Create the query terms from a list of terms
				self.query  = " ".join(query_terms)

				# Make and store a base64 encoded term
				self.query_b64 = base64.b64encode( self.query ) 

				# Generate the url from the query and query_b64
				self.url =  "http://www.commandlinefu.com/commands/matching/" + self.query + "/" + self.query_b64 + "/json/"

				# Encode the spaces too
				self.url = self.url.replace(" ","%20")
				

		def load( self ) :
				try :	
							#	Make request to the commandline fu API, split response by lines and print
							results  				= urllib2.urlopen(self.url)
							response_text	 	= results.read()
							
							# Create json file and return
							self.response_json = json.loads(response_text)				
							return self.response_json
							
				except urllib2.URLError, e:
						
						# In the event we have an Error we inform the user with/ colors
						errorStr = "%s: %s. Unable to connect to commandlinefu.com" %(color.cyan("cfu"), color.red("ERROR") )
						errorStr += "\n%s Possible network connection problem" % ( " "*len("cfu:") )
						sys.exit(errorStr) 


		def display ( self, isVerbose, count , showAll ) :

				self.total = len(self.response_json)

				# Check if we have any results, if inform user and exit
				if ( self.total  <1 ) :

						# Print with some red
						print "\t" + color.ok_blue(cfu) + ": No Results Matching Query"
						sys.exit(0)
				
				display_count = self.total if showAll else min(self.total,count)

				num = 1

				# Print each response
				for result in self.response_json[: display_count]:
						print ' %d\t# ' % num , result['summary']
						print '\t', result['command']
						if isVerbose :
								print '\tURL: ' , result['url']
								print '\tvotes: ', result['votes'] 
						print "\n"
						num += 1

				self.display_count = display_count
