def range(end, start=0, step=1):
    index = start
    while index < end:
        yield index
        index += step

some_range = range(10)
next_range = range(10)
for i in some_range:
    print(i)

#generator instances are one time use objects, so this will not print out anything
for i in some_range:
    print(i)

#this will print out stuff again
for i in next_range:
    print(i)
