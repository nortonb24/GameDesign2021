#Brenna Norton
#We are learning about list and tuples
#learn their funcions and looping with list 
myFruit=["apples, berries, mango, bannanas"]
print (myFruit)
for fruit in myFruit:
    print(fruit)

for fruit in myFruit: #for each element in the array get the element 
    print (fruit, end= " , ") #for the length of your array
    print()
counter=len(myFruit) #the length of your list is one more than your last index

for x in range (0,counter-1):
    print(myFruit[x], end= " , ")

    print(myFruit[counter-1]) #print the last element

if "apples" in myFruit:
    print ("Yes you got apples")
    myFruit.remove("apples")
    print(myFruit)
    myFruit.insert("0,kiwi")
    myFruit.insert("2,papaya")
    myFruit.append("beets")
    print(myFruit)