'''
Using ANSI Colors to print to terminal

Adapted from code taken from Blenders bcolor.py
Samir Ahmed 2012
'''

class color:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'

		CYAN  = "\033[36m"
		MAGENTA  = "\033[35m"
		RED  = "\033[31m"
		YELLOW  = "\033[33m"

		def disable(self):
				self.HEADER = ''
				self.OKBLUE = ''
				self.OKGREEN = ''
				self.WARNING = ''
				self.FAIL = ''
				self.ENDC = ''
		
		@staticmethod
		def cyan(string):
				return color.CYAN + string + color.ENDC
		
		@staticmethod
		def magenta(string):
				return color.MAGENTA + string + color.ENDC

		@staticmethod
		def red(string):
				return color.RED + string + color.ENDC

		@staticmethod
		def yellow(string):
				return color.YELLOW + string + color.ENDC

		@staticmethod
		def header(string):
				return color.HEADER + string + color.ENDC

		@staticmethod
		def fail(string):
				return color.FAIL + string + color.ENDC

		@staticmethod
		def warning(string):
				return color.WARNING + string + color.ENDC

		@staticmethod
		def blue(string):
				return color.OKBLUE + string + color.ENDC

		@staticmethod
		def green(string):
				return color.OKGREEN + string + color.ENDC

		@staticmethod
		def testAll( string ):
				print "HEADER  :\t" + color.header( string )
				print "OKBLUE  :\t" + color.blue( string)
				print "OKGREEN :\t" + color.green(string)
				print "CYAN    :\t" + color.cyan(string)
				print "RED     :\t" + color.red(string)
				print "MAGENTA :\t" + color.magenta(string)
				print "YELLOW  :\t" + color.yellow( string)
				print "WARNING :\t" + color.warning( string)
				print "FAIL    :\t" + color.fail( string)
				

