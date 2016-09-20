name = 'Dennis Ledwon'
age = 19
height = 180.0 #centimeters
height_in_meters = height / 100.0
weight = 67 #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "That equals %r meters." % height_in_meters
print "He's %d kilograms heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on coffe." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)