def number(x,operator,y):
    if operator=="+":
     return x+y
    if operator=="-":
       return x-y
    if operator=="*":
       return x*y
    if operator=="/":
       return x/y
    if operator=="%":
       return x%y
    if operator=="**":
       return x**y
x=int(input("enter the first number:"))
operator=input("enter the operator:")
y=int(input("enter the third number:"))
calculate=number(x,operator,y)
print (calculate)


    

