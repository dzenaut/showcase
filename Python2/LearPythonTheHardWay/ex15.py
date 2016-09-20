#imports module/library sys
from sys import argv

#splits argv into two variables, script and filename
script, filename = argv

#from open you get a file, and you can do things to it, such as read. Such a command is filed after a '.'
txt = open(filename)

#print filename
print "Here's your file %r:" % filename
#reads and prints without parameters (empty parentheses) the file (set to variable txt) that was just opened
print txt.read()
#important to close files again
txt.close()

print "Type the filename again: "
#user input of a filename set to variable file_again
file_again = raw_input("> ")

#txt_again set to the opened file_again
txt_again = open(file_again)

#reads and prints without parameters the file txt_again that was just opened
print txt_again.read()
#important to close files again
txt_again.close()