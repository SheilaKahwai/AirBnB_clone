#!/usr/bin/python3
"""
The Console Module
Serves as the entry point of our command interpreter.
"""


import cmd


class HbnbConsole(cmd.Cmd):
    """Our subclass of the Cmd class"""
    prompt = '(hbnb) '
	
    def do_quit(self, arg):
        """Exits the shell"""
        return True

    def help_quit(self):
        print("Exits the shell")

    def emptyline(self):
        """Overrides the emptyline method"""
        pass

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == '__main__':
    HbnbConsole().cmdloop()
    print()
