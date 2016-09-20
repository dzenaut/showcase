from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	#.readline() moves read head to the right after the \n that ends the line
	#without the comma (,) behind the print line that uses f.readline(), there would be double \n, the comma removes one
	print line_count, f.readline(),

current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "\nNow let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

#x = x + y is the same thing in python as writing x += y
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)