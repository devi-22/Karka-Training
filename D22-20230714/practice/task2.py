monthly_gold_rate=[{"month_name":"January",
                    "gold_rate":1500,
                    "jewel_list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                    "making_cost":14}]},
                    {"month_name":"Feburary",
                     "gold_rate":2000,
                     "jewel_list":[{"name":"chain",
                                    "making_cost":18},
                                    {"name":"ring",
                                     "making_cost":11}]},
                     {"month_name":"March",
                      "gold_rate":1000,
                      "jewel_list":[{"name":"chain",
                                     "making_cost":13},
                                     {"name":"ring",
                                      "making_cost":15}]},
                      {"month_name":"April",
                       "gold_rate":2500,
                       "jewel_list":[{"name":"chain",
                                      "making_cost":15},
                                      {"name":"ring",
                                       "making_cost":17}]},
                       {"month_name":"May",
                        "gold_rate":3000,
                        "jewel_list":[{"name":"chain",
                                       "making_cost":13},
                                       {"name":"ring",
                                        "making_cost":14}]}]

from pprint import pprint
pprint(monthly_gold_rate)
"""for i in monthly_gold_rate:
    print(i)"""
#print(monthly_gold_rate)

#rate_percentage=monthly_gold_rate[0]["jewel_list"][0]["making_cost"]*monthly_gold_rate[0]["gold_rate"]
"""rate_percentage=(monthly_gold_rate[0]["gold_rate"]*monthly_gold_rate[0]["jewel_list"][0]["making_cost"]/100)+monthly_gold_rate[0]["gold_rate"]
rate_percentage
print(rate_percentage)"""
"""for i in monthly_gold_rate:
    #print(i)
    #print("\n")
    for list in i["jewel_list"]:
        a=list["name"]
        percentage=(list["making_cost"]*i["gold_rate"]/100)+i["gold_rate"]
        
        #print(f"month:{i['month_name']}\ngold_rate:{i['gold_rate']}\n\t{a}:{percentage}")
        #print("\n")
        #print(percentage)
        list=[]
        dict={"month":i['month_name'],"gold_rate":i['gold_rate'],a:percentage}
        list.append(dict)
        print(list)
        print("\n")"""
        

        #print(list)
    
    


"""rate_min=monthly_gold_rate[0]["gold_rate"]
month_min=monthly_gold_rate[0]["month_name"]
rate_max=monthly_gold_rate[0]["gold_rate"]
month_max=monthly_gold_rate[0]["month_name"]
for i in monthly_gold_rate:

    if rate_min>i["gold_rate"]:
        rate_min=i["gold_rate"]
    if month_min>i["month_name"]:
        month_min=i["month_name"]
    if rate_max<i["gold_rate"]:
        rate_max=i["gold_rate"]
    if month_max<i["month_name"]:
        month_max=i["month_name"]
print(f"month: {month_min}\t gold_rate: {rate_min}")
print(f"month: {month_max}\t gold_rate: {rate_max}")"""

      


