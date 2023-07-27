name="Devipriya"
dic_name={"name":name}
print(dic_name)
"""days={"sunday","monday","tuesday"}
print(days)
print(days)
print(days)"""
file=open("/home/devipriya/Devipriya.txt","r")
print(file.read())
for line in file:
    print(line)
for data in file:
    data=file.read()
    print(data)
"""file=open("/home/devipriya/Devipriya.txt","w")
print(file.write("I'm Devipriya \n"))
print(file.write("Hi!Everyone"))
print(file.close())
file=open("/home/devipriya/Devipriya.txt","r")
print(file.read(8))
for line in file:
    print(line)"""
# file=open("/home/devipriya/Devipriya.txt","a")  
# print(file.write("age:21\n")) 
# print(file.write("place:Aralvaimozhi"))
# print(file.close())
file=open("/home/devipriya/Devipriya.txt","r")
# print(file.read())
for line in file:
    print(line.split())

