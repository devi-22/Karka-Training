a=4
for i in range(a):
     print("*"*a)
b=int(input("b: "))
for i in range(b):
     print("*"*b)
a=5 
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print("")

n=5
num=1
for i in range(n):
    for j in range(n):
        print(num,end=" ")
        num+=1
        print(" ")
n=5
for i in range(1,(n*n)+1):
    print(i,end=" ")
    if i%5==0:
        print("\n")
n=5
for i in range(n*n,0,-1):
    #print(i)
    if i%n==0:
        print(" ")
    print(i,end=" ")


    
    