leap_yr=int(input("enter a year"))
if (leap_yr%4==0 and leap_yr%100!=0 or leap_yr%400==0):
     print ("is a leap year")
else: 
     print ("is not a leap year")
