'''
def clip(lo, x, hi):
	if x < min(lo, hi):
		print min(lo, hi)
	elif x > max(lo, hi):
		print max(lo, hi)
	else:
		print x
'''

#return hi, if x>hi, returns lo, if x<lo, otherwise returns x
def clip(lo, x, hi):
	return min(max(lo, x), hi)

z = clip (7, 6, 10)
print z

