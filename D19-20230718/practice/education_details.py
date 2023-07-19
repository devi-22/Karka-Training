education_details=[{"study":"B.Tech",
                    "institute":"Cape",
                    "semester_marks":[{"semester_name":1,
                                      "subjects":["Computer Programming","Maths1","Datascience"],
                                      "semester_grade":"A"},
                                      {"semester_name":2,
                                       "subjects":["Datastructure","Oops","Maths2"],
                                       "semester_grade":"B"}]},
                                       {"study":"M.Tech",
                                        "institute":"PSN",
                                        "semester_marks":[{"semester_name":1,
                                                           "subjects":["Advanced Computer","Oriented Data Structure"],
                                                           "semester_grade":"A"},
                                                           {"semester_name":2,
                                                            "subjects":["Computer Network","Database System"],
                                                            "semester_grade":"B "}]}]
#print(education_details)
for item in education_details:
    #print(item)
    print(item["study"])   
semester_marks=item["semester_marks"]
for sem in semester_marks:
    #print(sem)
    print(sem["semester_name"])
    print(sem["subjects"])

