listnums=[]

for num in range(1000):
    if num%3==0 or num%5==0:
        listnums.append(num)

print(sum(listnums))
