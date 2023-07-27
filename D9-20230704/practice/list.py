#list
fruits=["apple","banana","orange","grapes","watermelon"]
print(fruits[1])
print(fruits[:2])
print(fruits[1:])
print (len(fruits))
#dictionary method
data={"top":200,
      "kurti":500,
      "saree":1000}
print(data["saree"])
print(len(data))
#iteration
fruits=["apple","orange","banana","grapes",
        "watermelon","guava","pineapple","mango",
        "lichi","stawbery","blueberry","greenapple"]
for i,fruit in enumerate (fruits):
    if(i<3):
        print(fruit)
    else:
        break
for i,fruit in enumerate(fruits):
    if(i+1)%4==0:
        print(fruit)
for i,fruit in enumerate(fruits):
    if(i>1):
        continue
    else:
        print(fruit)
#letters: output(d h l)
letters=["a","b","c","d","e","f","g","h","i","j","k","l"]
for i,letter in enumerate(letters):
    if(i+1)%4==0:
        print(letter)











    

