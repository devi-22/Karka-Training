consumer_data={"consumer_name":"devipriya",
               "eb_reading":[1100,1200,1350,1650,2050]}


def calculate_electricity_bill(consumer_data):
    List=[]
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
        dict={"month":i+1,"units_consumed":a, "bill_amount":value}
        List.append(dict)
    print(List)  
    return List
amount=calculate_electricity_bill(consumer_data)
"""for i in amount:
    print(i)
    print(f"month:{i['month']}\nunits_consumed:{i['units_consumed']}\nbill_amount:{i['bill_amount']}")
    print("\n")
dict=str(i)
file=open("/home/devipriya/devipriya.txt","a")
print(file.write(dict))"""
"""file=open("/home/devipriya/devipriya.txt","r")
print(file.read())"""
text=""
import json
name=str(list)
method=input("enter the method: ")
if method=="json" and "Json" and "JSON" and "jsOn" and "JSon":
    list_json=json.dumps(name)
    print(list_json)
elif method=="dict":
    list_dict=str(list)
    print(list_dict)
for i in list:
    text=text+(f"month:{i['month']},\nunits_consumed:{i['unit_consumed']},\nbill_amount:{i['bill_amount']}")
        








