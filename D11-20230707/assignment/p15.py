print("Think of something and I'll try to guess it !")
ques1=input("Question 1) Does it stay inside or outside or both?")
ques2=input("Question 2) Is it a living thing?")
if (ques1=="inside") and (ques2=="yes"):
    print("houseplant")
if (ques1=="outside") and (ques2=="no"):
    print("shower curtain")
if (ques1=="inside") and (ques2=="yes"):
    print("bison")
if (ques1=="outside") and (ques2=="no"):
    print("billboard")
if (ques1=="both") and (ques2=="yes"):
    print("dog")
if (ques1=="both") and (ques2=="no"):
    print("cellphone")
else:
    print("Then what else could you be thinking of besides a pyton!")
