def calc_interest(p,n,r):
    interest=p*n*r/100
    return interest
p=1000
n=10
r=2
interest=calc_interest(p,n,r)
print (interest)
#twice the number
def twice(a):
    b=a*2
    return b
a=10
b=twice(a)
print(b)    
#eligible check
def passed_out_yr(year):
    if year>=2022:
        return True
    else:
        return False
year=int(input("enter the year:"))
a=passed_out_yr(year)
print(a)





