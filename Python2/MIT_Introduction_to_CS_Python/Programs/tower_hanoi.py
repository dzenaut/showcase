def printMove(fr, to):
	print "move from", str(fr), "to", str(to)

def Towers(n, fr, to, spare):
	if n == 1:
		printMove(fr, to)
	else:
		#moves the whole stack - base disk to spare
		Towers(n-1, fr, spare, to)
		#moves the base disk to to
		Towers(1, fr, to, spare)
		#moves the whole stack back on top of base disk to to
		Towers(n-1, spare, to, fr)

Towers(3, "f", "t", "s")

'''
When you are talking about moving the (whole stack-1)
you are actually thinking about a procedure which breakes
this task into simple moves. Let us think about it in
another way. It is obvious that to move the lowest disk 
first you need to move all the smaller ones. And they need 
to be moved to a spare position, otherwise you can not move 
the lowest disk to the destination (you will put it on top 
	of smaller ones). Once you've put the biggest disk in 
the correct position you can ignore it: whatever you do 
with the other disks they can freely be put on top of this 
biggest disk. Thus all that is left to do is to move the 
rest of the disks on top of the bigger disk.
Let us say, then, that there is a sequence of simple moves 
(one disk at a time) which solves the initial problem of 
moving the whole stack. According to what I previously 
wrote, the first part of the sequence as a whole will 
actually solve the problem of moving the whole stack-1 
to the spare position. Then you move the biggest disk. 
The rest of the moves can be grouped together as solving 
the problem of moving the whole stack-1 on top of the biggest 
disk. After that the subsequence of moves for the smaller
problem can be divided further.
'''