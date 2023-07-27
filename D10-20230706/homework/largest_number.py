#find largest number in list don't use in-built function 
numbers=[1,100,300,4]
def largest(numbers):
    large=numbers[0]
    for i in numbers:
        if i>large:
            large=i
    return large
a=largest(numbers)
print(a)





        
        