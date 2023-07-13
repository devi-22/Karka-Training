passed_out_yr=input ("which year you passed out from college")
print (passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print (type_of_passed_out_yr)
passed_out_yr=int(passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print (type_of_passed_out_yr)
#NOT operation
long_hair=True
is_eligible=not long_hair
if is_eligible:
        print("the student is eligible")       
else:
    print("the student is not eligible")
#OR opration
is_eligible=passed_out_yr==2022 or passed_out_yr==2023
print (is_eligible)





