dup_value=[1,2,3,2,5,1,5]
value=[]
for i in dup_value:
    if i not in value:
        value.append(i)
print("original_value = ",value)            

x=bin(36)
x=bin(10)
print(x)
x=abs(-7.25)
x=abs(2+8j)
print(x)
x=dict(name="devi",age=21,place="aral")
print(x)
x="print(95)"
eval(x)
x=format(0.05,"%")
print(x)
x=("apple","banana","cherry")
x=("devi")
y=id(x)
print(y)
x=(1,3)
a=sum(x)
print(a)
passed_out_yr=int(input("year"))
def devi(passed_out_yr):
    if passed_out_yr>2021:
        return True
    else:
        return False
b=devi(passed_out_yr)
print(b)