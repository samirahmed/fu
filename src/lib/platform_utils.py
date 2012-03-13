""" 
		Platform Interface utility
			
"""
import webbrowser
import subprocess
import commands
import platform
import shlex
from terminalColor import color

class system:

		def __init__(self):
				
				info = set( [ ss.lower() for ss in platform.uname() ])
				
				# determine the type of platform
				
				if 'cygwin' in info:
						self.name = 'windows'
						self.copy_command = 'clip'
				elif 'darwin' in info:
						self.name = 'mac'
						self.copy_command = 'pbcopy'
				else :
						self.name = 'linux'
						self.copy_command = 'xclip -selection clipboard'

		"""Copy given string into system clipboard."""
		def copy(self,string):

				# Assuming it works, we try and execute the function
				worked = True
				try:
						subprocess.Popen(shlex.split(self.copy_command), stdin=subprocess.PIPE).communicate(str(unicode(string)))
				except Exception, why:

						# If it doesn't work return flase
						worked = False
						print "%s: %s. The %s command failed" % ( color.cyan('fu'), color.fail('ERROR'), self.copy_command ) 
				return worked
			 

		""" Open the command in the clipboard """
		def open(self,string):

	 		# We will attempt to open the url
			try:
				webbrowser.open(string)
			except:
				print "%s: %s. \n\t%s" % (color.cyan('fu'), color.fail('Unable to Open Browser' ) , string)
		
		def paste(self):
				"""Returns system clipboard contents."""
				try:
						return unicode(commands.getoutput('pbpaste'))
				except Exception, why:
						raise XcodeNotFound
