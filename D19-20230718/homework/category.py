items_list=[{"name":"Apple","category":"fruits"},
            {"name":"Carrot","category":"vegetables"},
            {"name":"Banana","category":"fruits"},
            {"name":"Broccoli","category":"vegetables"}]
fruits=[]
vegetables=[]
for item in items_list:
    if item["category"]=="fruits":
        fruits.append(item["name"])
    if item["category"]=="vegetables":
        vegetables.append(item["name"])
dict_names={"fruits":fruits,"vegetables":vegetables}
print(dict_names)   

