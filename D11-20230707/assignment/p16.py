gender=input("What is your gender? (male or female):")
name1=input("first name:")
name2=input("last name:")
age=int(input("age:"))
ques1=input(f"\nAre you married,{name1} (yes or no)? ")
if (gender=="female") and  (age>=20) and (ques1=="yes"):
    print(f"Then I shall call you Mrs.{name2}.")
if (gender=="female") and (age>=20) and (ques1=="no"):
    print(f"Then I shall call you Ms.{name2}.")
if (gender=="female") and (age<20) and (ques1=="no"):
    print(f"Then I shall call you Ms.{name2}.")
if (gender=="female") and (age<20) and (ques1=="yes"):
    print(f"Then I shall call you Mrs.{name2}.")
if (gender=="male") and (age>=20) and (ques1=="yes"):
    print(f"Then I shall call you Mr.{name2}.")
if (gender=="male") and (age<20) and (ques1=="yes"):
    print(f"Then I shall call you Mr.{name2}.")
else:
    print("not found")
