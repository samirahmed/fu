import os
import json

''' 	dotfile is a class for managing the local dotfile storage 
			
			saves a file called, '.fu' to your home directory
			the file is format a json file
			
			{ 
				result	: Last Search Result
				last		: Last Copied command
				history	: History of used commands
			}

			the entire dot file is rewritten on every write

'''
class dotfile:
		
		''' Initialize the dotfile '''
		def __init__(self):
				self.path = os.path.join(os.getenv("HOME"),'.fu')
				self.__load()
				self.history_size = 30

		''' Get the history of all the copied command '''
		def history(self):
				return self._history
				
		''' Get the command that was copied'''
		def last(self):
				return self._last

		''' Get the last search result '''
		def result(self):
				return str(self._result)

		''' Save the search result dotfile '''
		def save_result(self,string):
				self._result = string

		''' Copy will add the string to be copied to the dotfile '''
		def save_copy(self,string):
				self._last = string
				self.__record(string)
		
		''' Record will add a command to the history '''
		def __record(self,string):

				# If we are at capacity, remove
				if len(self._history) >= self.history_size : 
						self._history = self.history[:used_size]
				
				# Prepend to the history
				self._history.insert(0,string)

		''' Private file for loading the dotfile '''
		def __load(self):
				
				# If the file doesn't exist make it
				if not os.path.isfile(self.path):
						self.__make()
			  # Read the file name	
				fid = open(self.path, 'r')
				raw = fid.read()
				fid.close()

				# Check if we have the json objects we are looking for
				self._storage = json.loads(raw)

				if 'result' in self._storage :
						self._result = str (self._storage['result'])
				else :
						self._result = ""
				
				if 'last' in self._storage:
						self._last = self._storage['last']
				else :
						self._last = "" 
				
				if 'history' in self._storage :
						self._history = self._storage['history']
				else :
						self._history = [];
				
		''' Private helper for making an empty json file '''
		def __make(self):
				fid = open( self.path ,'w') 
				fid.write("{}")
				fid.close()

		def save(self):
				savefile = json.dumps({	'result' : self._result, 'history' : self._history , 'last' :  self._last } ) 
				fid = open(self.path, 'w')
				fid.write(savefile)
				fid.close()

