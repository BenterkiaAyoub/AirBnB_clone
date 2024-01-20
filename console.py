#!/usr/bin/python3

"""
This is a sample console script.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Show help message."""
        print("Documented commands (type help <topic>):")
        print("=========================================")
        print("EOF  help  quit")

    def do_EOF(self, arg):
        """Exit the console."""
        print("")
        return True

    def do_quit(self, arg):
        """Exit the console."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

