from cmd import Cmd


"""
The Console Module
Serves as the entry point of our command interpreter.
"""


class HbnbConsole(Cmd):
	"""Our subclass of the Cmd class"""
	prompt = '(hbnb) '
	
	def do_quit(self, arg):
		"""Exits the shell"""
		self.close()
		return True

	def help_quit(self):
		print("Exits the shell")

	do_EOF = do_quit
	help_EOF = help_quit

if __name__ == '__main__':
    	HbnbConsole().cmdloop()
