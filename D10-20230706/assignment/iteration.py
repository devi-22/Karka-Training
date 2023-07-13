numbers=[10,20,40,30,40]
total_numbers=0
for i,number in enumerate(numbers):
    print("before",total_numbers)
    total_numbers=total_numbers+number
    print("after",total_numbers)
print(total_numbers)
for i,number in enumerate(numbers):
    average=(total_numbers/len(numbers))
    print("before",average)
    average=(total_numbers/len(numbers))
    print("after",average)
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enumerate(numbers):
    print("entering the first iteration process for item:"+str(i))
    print("before ",total_numbers)
    total_numbers=total_numbers+number
    print("after ",total_numbers)
    print("exiting iteration process for item:"+str(i))
    print("\n")
prods=[500,200,700,1000]
currency_code="INR"
list=[]
for prod in prods:
    a=currency_code+str(prod)
    list.append(a)
print(list)
    


    



    






    






