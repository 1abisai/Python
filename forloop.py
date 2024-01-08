for i in range(151):
    print(i)

#multiple of five

for i in range(0, 201):
    print(i*5)

#counting dojo

for i in range(0, 101):
    if i%5==0:
      print("Coding")
    if i%10==0:
       print("Coding Dojo")
    print(i)

#ood number

total = 0

for i in range(0, 500000+1):
    if(i%2 !=0):
        print(i)
        total = total + i
print(total) 

#byfour

i = 2018
while i > 0:
        print (i)
        i = i - 4

#flex
lowNum = 2

highNum = 9

mult = 2

for i in range (lowNum, highNum):
        if i % mult == 0:
            print (i)