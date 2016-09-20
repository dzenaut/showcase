'''
functions:
	- name pieces of code the way variables name strings and numbers
	- they take arguments the way your script takes argv
	- let you make mini-scripts or tiny commands
	- created by using the word def
'''

#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

'''
define a function by def name_of_function(arguments)
	---> beware: need the asterisk in *args inside parentheses
		---> takes all arguments to the function
	---> end line with a colon and start indenting
		---> all indented lines become attached to name_of_function
		---> first line unpacks arguments
