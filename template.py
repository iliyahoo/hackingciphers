# doing execfile() on this file will alter the current interpreter's
# environment so you can import libraries in the virtualenv
activate_this_file = "/home/iliya/repositories/hackingciphers/bin/activate_this.py"

execfile(activate_this_file, dict(__file__=activate_this_file))