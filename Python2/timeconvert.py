time = int(raw_input("Enter minutes! "))
print

while time < 0:
	time = int(raw_input("Please enter a positve number for minutes! "))
	
	
hours = time/60
minutes = time%60

print time, "minutes converts to", hours, "hours and", minutes, "minutes!"