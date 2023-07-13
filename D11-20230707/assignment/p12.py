quiz=input("Are you ready for a quiz?")
if (quiz==True):
    print("okay,here it comes!")
else:
    print("not found")
ques1=int(input("Q1) ICICI is the name of a?\n\t1)chemical industry\n\t2)corporation\n\t3)financial institution\n>"))
question=0
question=question+1
correct_ans=0
if (ques1==3):  
    correct_ans=correct_ans+1
    print("That's right")
else:
    print("not found")
ques2=int(input("Q2) Can you store the value 'cat' in a variable of type int?\n\t1)yes\n\t2)no\n>"))
question=question+1
if (ques2==1):
    print("Sorry, 'cat' is a string. ints can only store numbers.")
else:
    correct_ans=correct_ans+1
    print("That's right")
ques3=int(input("Q3) What is the result of 9+6/3?\n\t1)5\n\t2)11\n\t3)15/3\n>"))
question=question+1
if (ques3==2):
    correct_answer=correct_ans+1
    print("That's right")
else:
    print("not found")
print(f"Overall,you get{correct_answer} out of {question}correct.\nThanks for playing!")
