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
				return ''.join([color.CYAN, string, color.ENDC])

		@staticmethod
		def magenta(string):
				return ''.join([color.MAGENTA, string, color.ENDC])

		@staticmethod
		def red(string):
				return ''.join([color.RED, string, color.ENDC])

		@staticmethod
		def yellow(string):
				return ''.join([color.YELLOW, string, color.ENDC])

		@staticmethod
		def header(string):
				return ''.join([color.HEADER, string, color.ENDC])

		@staticmethod
		def fail(string):
				return ''.join([color.FAIL, string, color.ENDC])

		@staticmethod
		def warning(string):
				return ''.join([color.WARNING, string, color.ENDC])

		@staticmethod
		def blue(string):
				return ''.join([color.OKBLUE, string, color.ENDC])

		@staticmethod
		def green(string):
				return ''.join([color.OKGREEN, string, color.ENDC])

		@staticmethod
		def testAll( string ):
				print "HEADER  :\t %s" % color.header( string )
				print "OKBLUE  :\t %s" % color.blue( string)
				print "OKGREEN :\t %s" % color.green(string)
				print "CYAN    :\t %s" % color.cyan(string)
				print "RED     :\t %s" % color.red(string)
				print "MAGENTA :\t %s" % color.magenta(string)
				print "YELLOW  :\t %s" % color.yellow( string)
				print "WARNING :\t %s" % color.warning( string)
				print "FAIL    :\t %s" % color.fail( string)


