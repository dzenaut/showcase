
tf = open('ab.txt')
count = 0
for line in tf.readlines():
	count += 1
	words = line.split()
	print('Line', count, ':', len(words))
tf.close()
