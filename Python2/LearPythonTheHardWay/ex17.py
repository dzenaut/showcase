from sys import argv
#can import the command exists, which checks if a file exists, based on its name in a string as an argument
#from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

'''in_file = open(from_file)
indata = in_file.read()'''

#brings lines 9-10 into one line and does not require closing of the file in the end anymore
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

'''print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()'''

out_file = open(to_file, 'w')
out_file.write(indata)

#print "Alright, all done."

out_file = open(to_file)
print out_file.read()


out_file.close()
#in_file.close()

'''in terminal you can make text files by using:
	echo "string" > name_of_new_file
then you can view the file with:
	cat name_of_new_file'''