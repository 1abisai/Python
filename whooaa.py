total = 0

for i in range(0, 500000+1):
    if(i%2 !=0):
        print(i)
        total = total + i
print(total)        