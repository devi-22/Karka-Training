names=[{"name":"Devipriya",
        "place":"Aralvaimozhi",
        "hobbies":["Listening Music","Playing Dogs","Watching TV"],
        "sslc":{"tamil":93,
                "english":77,
                "maths":92,
                "science":94,
                "social":98}},
                {"name":"Reshma",
                 "place":"Marthandam",
                 "honbbies":["Listening Music","Cooking","Gardening"],
                 "sslc":{"tamil":88,
                         "english":92,
                         "maths":77,
                         "science":98,
                         "social":100}}]
for name in names:
    tamil=(name["sslc"]["tamil"])
    english=(name["sslc"]["english"])
    maths=(name["sslc"]["maths"])
    science=(name["sslc"]["science"])
    social=(name["sslc"]["social"])
    total=tamil+english+maths+science+social
    print(total)
    

    average=total/5
    print(average)

    if (average)>90:
        print(name,"They are eligible for Maths Biology")
    if (average)>80 and (average)<=90:
        print(name,"They are eligible for Computer Science")
    if (average)>75 and (average)<=80 and (maths)<98:
        print(name,"They are eligible for Maths Biology")
    if (average)>70 and (maths)>98:
        print(name,"They are eligible for Computer Science ")
                        
