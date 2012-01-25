import urllib2
import sys
import base64
import time

# Start time
start = int(round(time.time() * 1000))

# Maximum number of commands to display
commandMAX = 3;

def main():		
		
# Create query from commandline args
		query = ""
		for terms in sys.argv[1:] :
				query+= terms + " "
		query = query[: len(query)-1]

# Get the base 64 encoded query
		b64 = base64.b64encode(query)

		url =  "http://www.commandlinefu.com/commands/matching/" + query + "/" + b64 + "/plaintext/"
		url = url.replace(" ","%20")

#	Make request to the commandline fu API, split response by lines and print
		try :
					results  = urllib2.urlopen(url)
					text 		 = results.read()
					printResponse (text.split("\n"))
					duration =  int(round(time.time() * 1000)) -  start
					print "\t%dms total:%d" % ( duration, text.count("#")-1 )
		except urllib2.URLError, e:
				print "cfU: ERROR. Unable to fetch search results" 

def printResponse ( lines ) :
		
# If there are less than 3 lines return
		if ( len(lines) <4) :
				print "\tcfu: No Results Matching Query"
				return

# prints an array of strings, skipping the first line 
		commandCount = 0
		for ll in lines[1:] :
				if len(ll) >0 and ll[0] == '#' :
						commandCount +=1
						if commandCount > commandMAX:
								break
				print "\t" + ll

# Print help instructions
def helpprint():
		
		print "\n\t'cfu' is a tool for searching http://www.commandlinefu.com  \n"
		print	"\tUSAGE: $cfu <search query>"
		print "\te.g	:	$cfu uuencode mail \n"
		print "\tThis will return a list of results matching your search \n"


if __name__ == "__main__":
		if len(sys.argv) == 1 :
				print "cfu: Incorrect usage, please include search terms. See 'cfu --help' " 
		elif (sys.argv[1] == "--help") or (sys.argv[1] == "-h") :
				helpprint()
		else :
				main( )
