"""consumer_data={"consumer_name":"devipriya",
               "eb_reading":[1100,1200,1350,1650,2050]}
readings=[1100,1200,1350,1650,2050]
readings=consumer_data["eb_reading"]
print(len(readings))
for i in range(1,len(readings)):
    units=readings[i]-readings[i-1]
    #print(units)
#for i in units:
    if (units<100):
        print("there is no amount to pay")
    if (units>100) and (units<200):
        unit1=2*units
        print(unit1)
    if (units>200) and (units<500):
        unit2=5*units
        print(unit2)
    if (units>500) and (units<1000):
        unit3=10*units
        print(unit3)
    if (units>1000):
        unit4=14*units
        print(unit4)
total=unit1+unit2+unit3+unit4
print("total",total)
dict=[{"month":1,"unit_consumed":units,"bill_amount":unit1},
      {"month":2,"unit_consumed":units,"bill_amount":unit2},
      {"month":3,"unit_consumed":units,"bill_amount":unit3},
      {"month":4,"unit_consumed":units,"bill_amount":unit4}]
print(dict)
print("totala amount",total)"""
consumer_data={"consumer_name":"devipriya",
               "eb_reading":[1100,1200,1350,1650,2050]}

# def calculate_electricity_bill(consumer_data):
#     month=0
#     bill=0
#     for i in range(0,len(consumer_data['eb_reading'])-1):
#         month=i+1
#         a=consumer_data["eb_reading"][i+1]-consumer_data['eb_reading'][i]
#         # print(a)
#         if a<100:
#             print(f"month:{month}\nunits_consumed:{a}\nbill_ammount:{bill}")
#         elif a>=100 and a<200:
#             value=a*2
#             bill=bill+value
#             print(f"month:{month}\nunits_consumed:{a}\nbill_amount{value}")
#         elif a>=200 and a<500:
#             value=a*5
#             bill=bill+value
#             print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")
#         elif a>=500 and a<1000:
#             value=a*10
#             bill=bill+value
#             print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")
#         else:
#             value=a*10
#             bill=bill+value
#     print(f"total amount:{bill}")
# calculate_electricity_bill(consumer_data)




def calculate_electricity_bill(consumer_data):
    units=[]
    month=0
    bill=0
    for i in range(0,len(consumer_data['eb_reading'])-1):
        month=i+1
        a=consumer_data["eb_reading"][i+1]-consumer_data['eb_reading'][i]
        #print(a)
        if a<100:
            print(f"month:{month}\nunits_consumed:{a}\nbill_ammount:{bill}")
        elif a>=100 and a<200:
            value=a*2
            bill=bill+value
            print(f"month:{month}\nunits_consumed:{a}\nbill_amount{value}")
        elif a>=200 and a<500:
            value=a*5
            bill=bill+value
            print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")
        elif a>=500 and a<1000:
            value=a*10
            bill=bill+value
            print(f"month:{month}\nunits_consumed:{a}\nbill_amount:{value}")
        else:
            value=a*10
            bill=bill+value
        dict={"month":i+1 ,"units_consumed":a, "bill_amount":value}
        units.append(dict)
    print(units)  
calculate_electricity_bill(consumer_data)
            
         

    



        


    






