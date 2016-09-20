a=0
b=1

evenfib=[]

while True:
    a,b=b,a+b
    if b>4000000:
        break
    evenfib.append(b)

final=[]

for num in evenfib:
    if num%2==0:
        final.append(num)

print(final)

print(sum(final))
