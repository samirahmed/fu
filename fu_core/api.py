#!/usr/bin/python

'''
The CommandLineFu API is documented at
->	http://www.commandlinefu.com/site/api/

Website and API are managed by David Winterbottom.
The API documentation states that all request must be in the following form
http://www.commandlinefu.com/commands/<command-set>/<format>/

This file will use it as follows

-format = json
-command-set = matching/ssh/c3No/sort-by-votes/ - Search results for the query 'ssh' (note that the final segment is a base64-encoding of the search query)

Written by Samir Ahmed 2012
'''

import sys
import json
import urllib2
import base64
from terminalColor import color
from cache import TimedResultDict

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
				self.url =  "http://www.commandlinefu.com/commands/matching/" + self.query + "/" + self.query_b64 + "/sort-by-votes/json/"

				# Encode the spaces too
				self.url = self.url.replace(" ","%20")

				# Enable cache
				self.cache = TimedResultDict.load()

		def load_with_cache( self ):
				self.response_json = self.cache.get_and_update(self.query, self.load)
				self.raw_json = json.dumps(self.response_json)
				return self.response_json

		def load( self ) :
				try :
							#	Make request to the commandline fu API, split response by lines and print
							### In case of proxy requirement ###
							##
							#    os.environ['http_proxy'] = '$hostname:$port'
							#    os.environ['no_proxy'] = '$hostname'
							#
							urllib2.install_opener(
										urllib2.build_opener(
													urllib2.ProxyHandler()
										)
							)
							headers = {
										'User-Agent': r'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7',
										'Accept-Encoding':'gzip, deflate'
							}
							req = urllib2.Request(self.url, headers=headers)
							results  				= urllib2.urlopen(req)
							response_text	 	= results.read()
							if 'gzip' in results.headers.get('Content-Encoding', ''):
										import zlib
										response_text = zlib.decompress(response_text, 16+zlib.MAX_WBITS)
							import re
							m = re.search(r'\[.*\]', response_text) ### make sure only json array.
							response_text = m.group(0)
							self.raw_json 	= response_text
							# Create json file and return
							self.response_json = json.loads(response_text)
							return self.response_json

				except urllib2.URLError, e:

						# In the event we have an Error we inform the user with/ colors
						errorStr = "%s: %s. Unable to connect to commandlinefu.com" %(color.cyan("fu"), color.red("ERROR") )
						sys.exit(errorStr)

		''' print api response function '''
		def display ( self, isVerbose, count , showAll ) :

				self.total = len(self.response_json)

				# Check if we have any results, if inform user and exit
				if ( self.total  <1 ) :

						# Print with some red
						print  color.cyan('fu') + ": No Results Matching Query"
						sys.exit(0)

				display_count = self.total if showAll else min(self.total,count)

				num = 1

				# Print each response
				for result in self.response_json[: display_count]:

						# Extract the summary and commands
						summary =  result['summary']
						command = color.green(result['command'])

						# Highlight any of the search terms
						summary = self.__highlight( summary )

						# Highlight any of a
						print ' %s\t# ' % color.cyan(str(num)) , summary
						print '\t', command

						if isVerbose :
								print '\tURL: ' , result['url']
								print '\tvotes: ', result['votes']
						print ""
						num += 1
				self.display_count = display_count

		'''
				Highlight will find loosely matching search terms and color them

				Do a find and replace for strings for possible permutations
				Replace of exact matches
				Replace all capitalized matches
				Replace all whitespace bounded terms with any capitalization
		'''
		def __highlight( self, sentence ):


				# Straight forward find and replace
				for words in self.search_terms:

						sentence = sentence.replace(words,color.yellow(words))
						sentence = sentence.replace(words.capitalize(),color.yellow(words.capitalize()))

				# In case of difficult capitalization, e.g YouTube, we make a set terms
				query_set = set( [  terms.lower() for terms in self.search_terms ])

				# Check if words match in the lower case, if so color the original word
				for words in sentence.split():
						if words.lower() in query_set:
								sentence = sentence.replace(words,color.yellow(words))

				return sentence



