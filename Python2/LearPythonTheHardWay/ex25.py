def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

'''
lists.pop([i]) remove the item at the given position and return it.
If no index is given, the last object of the list is removed and returned
'''

def print_first_word(words):
	word = words.pop(0)
	print word

def print_last_word(words):
	#no index in .pop() means that the last word is removed and returned
	word = words.pop()
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

'''
if the file is run in the terminal, typin ex25 all the time is annoying
That's why it makes sense to write from ex25 import * 
The * means that everything is imported from ex25
'''