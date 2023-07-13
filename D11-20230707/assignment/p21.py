import p7
height=float(input("Your height in m:"))
weight=int(input("Your weight is kg:"))
BMI=p7.BMI(weight,height)
if (BMI<18.5):
    print("BMI Catagory: underweight")
elif (BMI>=18.5) and (BMI<=24.9):
    print("BMI Category: normal weight")
elif (BMI>=25.0) and (BMI<=29.9):
    print("BMI Category: overweight")
elif (BMI>=30.0):
    print("BMI Category: obese")
else:
    print("not found")

    
