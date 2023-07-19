my_resume={"name":"Devipriya.R",
            "e-mail":"devipriya733945@gmail.com",
            "mobile-no":"7339452128",
            "soft_skills":["Teamwork","Active Listening","Writing"],
            "hard_skills":["Bookkeeping","Copywriting"],
            "educational_qualification":[
                {
                "qualification":"SSLC",
                "total_mark":454,
                "percentage":91,
                "passed_out_yr":2017},
                {"qualification":"HSC",
                 "total_mark":373,
                 "percentage":62,
                 "passed_out_yr":2019},
                 {"degree":"B.E",
                  "percentage":75,
                  "passed_out_yr":2023}
                  ],
                "projects":{
                      "project":["Planning Analysis and Design of Cantilever Bridge","Experimental Investigation of Testing the Suitability of Beach Sand as Fine Aggregate"],
                      "source":["Products and Material","Tools and Equipment"]},
                      "experience":[{
                          "company_name":"Jeyam Construction",
                          "role":"Site Engineer",
                          "duration":1.4},
                          {"company_name":"MH Construction",
                           "role":"Construction Manager",
                           "duration":1},
                           {"company_name":"RD Construction",
                            "role":"Site Engineer",
                            "duration":1.8}],
                           "hobbies":["Reading Books","Playing Dogs","Listening Music"],
                           "personal_details":[{
                           "father's_name":"P.Rajadurai",
                           "father's_occupation":"Shop Owner",
                           "languages_known":["Tamil","English"],
                           "DOB":"16-02-2002",
                           "gender":"female",
                           "martial_status":"Single",
                           "address":{
                               "door_no":"80A1",
                               "street_name":"Villavilai",
                               "place":"Aralvaimozhi",
                               "district":"Kanyakumari",
                               "pincode":"629 301"}}]}
#print(my_resume)
for i in my_resume["educational_qualification"]:
    #print(i)
    print(i["percentage"])
for i in my_resume["personal_details"]:
    #print(i)
    print(i["languages_known"])
    print(i["address"]["street_name"])

    
