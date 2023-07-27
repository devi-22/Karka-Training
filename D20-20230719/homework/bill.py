consumer_data={"consumer name":"devipriya",
               "meter_reading":[1100,1200,1350,1650,2050]}
readings=[1100,1200,1350,1650,2050]
def calculate_electricity_bill(consumer_data):
    readings=consumer_data["meter_reading"]
    list=[]
    for i in range(len(readings)-1):
        bill_amount=0
        month=0
        units=readings[i+1]-readings[i]
        #print(units)
        month=i+1
        if units<100:
            print(f"month:{month}\nunits_consumed{units}\nbill_amount{bill_amount}")
        if units>=100 and units<200:
            value=units*2
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed:{units}\nbill_amount:{value}")
        if units>=200 and units<500:
            value=units*5
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed:{units}\nbill_amount:{value}")
        if units>=500 and units<1000:
            value=units*10
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed:{units}\nbill_amount:{value}")
        if units>=1000:
            value=units*14
            bill_amount=bill_amount+value
            print(f"month:{month}\nunits_consumed:{units}\nbill_amount:{value}")

        dict={"month":month,"units_consumed":units,"bill_amount":bill_amount}
        #print(dict)
        list.append(dict)
        #print(list)
    total=0
    total=total+bill_amount
    print("total amount",total)
#calculate_electricity_bill(consumer_data)
    
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
    
    """for i in list:
        text=text+(f"month:{i['month']},\nunits_consumed:{i['unit_consumed']},\nbill_amount:{i['bill_amount']}")
        file_name="/home/devipriya/devipriya.txt"
        with open(file_name,"w")as file:
            file.write(list_json)
            file.write(list_dict)"""



    






