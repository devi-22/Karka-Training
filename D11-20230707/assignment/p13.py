animal1="squirrel"
animal2="moose"
vegetable1="carrot"
vegetable2="watermelon"
mineral1="paper clip"
mineral2="camero"
print("Think of an object, and I'll try to guess it.\n")
ques1=input("Question 1) Is it animal,vegetable or mineral?\n>")
ques2=input("Question 2) Is it bigger than a breadbox?\n>")
bread_box="no"
if (ques1=="animal") and (ques2=="yes"):
    print(f"My guess is that you are thinking of a {animal1}.\nI would ask you if I'm right,but I don't actually care.")
elif (ques1=="animal") and (ques2=="no"):
    print(f"My guess is that you are thinking of a {animal2}.\nI would ask you if I'm right,but I don't actually care.")
elif (ques1=="vegetable") and (ques2=="yes"):
    print(f"My guess is that you are thinking of a {vegetable1}.\n.I would ask if I'm right, but I don't actually care.")
elif (ques1=="vegetable") and (ques2=="no"):
    print(f"My guess is that you are thinking of a {vegetable2}.\nI would ask if I'm right, but I don't actually care.")
elif(ques1=="mineral") and (ques2=="yes"):
    print(f"My guess is that you are thinking of a {mineral1}.\nI would ask if I'm right, but I don't actually care.")
elif (ques1=="moineral") and (ques2=="yes"):
     print(f"My guess is that you are thinking of a {mineral2}.\nI would ask if I'm right, but I don't actually care.")
