venus=0.78
mars=0.39
jupiter=2.65
saturn=1.17
uranus=1.05
neptune=1.23
earth_gravity=int(input("Please enter your current earth weight:"))
print("I have information for the following planets:\n\t 1.venus\t 2.mars\t  3.jupitar\n\t 4.saturn\t 5.uranes 6.naptune")
visit=int(input("Which planet are you visiting:"))
if visit==1:
    weight=(earth_gravity*venus)
    print(f"Your weight would be  {weight} pounds on that planet.")
if visit==2:
    weight=(earth_gravity*mars)
    print(f"Your weight would be {weight} pounds on that planet.")
if visit==3:
    weight=(earth_gravity*jupiter)
    print(f"Your weight would be {weight} pounds on that planet.")
if visit==4:
    weight=(earth_gravity*saturn)
    print(f"Your weight would be {weight} pounds on that planet.")
if visit==5:
    weight=(earth_gravity*uranus)
    print(f"Your weight would be {weight} pounds on that planet.")
if visit==6:
    weight=(earth_gravity*neptune)
    print(f"Your weight would be {weight} pounds on that planet.")
