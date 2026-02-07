#CODE:
a = int(input())
for i in range(1,a):
    for j in range(1,a):
        if j==a-i or i==j:
            print(" ",end=" ")
        else:
            print("0",end=" ")
    print()
#INPUT:
6
#OUTPUT:
'''
  8 8 8   
8   8   8 
8 8   8 8 
8   8   8 
  8 8 8   
'''
