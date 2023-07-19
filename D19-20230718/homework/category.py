items_list=[{"name":"Apple",
             "category":"Fruits"},
             {"name":"Carrot",
              "category":"Vegetables"},
              {"name":"Banana",
               "category":"Fruits"},
               {"name":"Broccoli",
                "category":"Vegetables"}]
"""fruits_name=["Apple","Banana"]
vegetables_name=["Carrot","Broccoli"]
dic_name={"fruits":fruits_name,
          "vegetables":vegetables_name}
print(dic_name)"""
fruits=[] 
vegetables=[]
for item in items_list:
    if (item["category"]=="Fruits"):
        item[category].append(item[name])
        print(item)

    
    
    
    """if (fruits==item["category"]):
        a=(item["category"],item["name"])
        fruits.append(a)
        print(fruits)"""