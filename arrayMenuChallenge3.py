# Method Description​
# append() Adds an element at the end of the list​
# clear() Removes all the elements from the list​
# copy() Returns a copy of the list​
# count() Returns the number of elements with the specified value​
# extend() Add the elements of a list (or any iterable), to the end of the current list​
# index() Returns the index of the first element with the specified value​
# insert() Adds an element at the specified position​
# pop() Removes the element at the specified position​
# remove() Removes the item with the specified value​
# reverse() Reverses the order of the list​
# sort() Sorts the list​

#Brenna Norton
# Create a list of at least 5 elements (or ask the user to give the Values)
# Create a menu similar to what we did for the Strings MEthods
# in each selection you will allow the user to:
# 1 insert elements either appending or inserting
# 2 delete an element either by value or by index
# 3  find if something in the list
# 4  Find the index where an element is in the list
# 5 reverse th eorder of the array
from typing import Text
ComputerParts=["keyboard", "mouse", "camera", "screen", "charger"]
L1=('***********************************')
L2=('*       My Game                   *')
L3=('*        Menu                     *')
L4=('*      1.insert                   *')
L5=('*      2.delete                   *')
L6=('*      3.find value               *')
L7=('*      4.find index               *')
L8=('*      5.reverse                  *')        
L9=('*      6.Exit                     *') 
L10=('**********************************')
def menu():
    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print(L5)
    print(L6)
    print(L7)
    print(L8)
    print(L9)
    print(L10)
    print('enter a selction 1-6')
    inputNumber = input()
    x=int(inputNumber)
    return x
def pause():
    print("Do you want to do this again?")
    answer1= input()
    answer1= answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False
x=1
while x !=7: #loop is conditioned to an event 
    x=menu() #expecting a return value
    if x==1:
        print("Level 1")
        capitalize=True #Boolean variable 
        while capitalize:
            print()
            print('What element would you like to add?')
            answer=input()
            ComputerParts.append(answer)
            print(ComputerParts)#is a method of string you have to refer with 
            capitalize=pause()
    if x==2:
        print ("Level 2")
        upper=True
        while upper:
            print()
            print(ComputerParts)
            print('What would you like to delete?')
            answer=input()
            ComputerParts.remove(answer)
            print(ComputerParts)#is a method of string you have to refer with 
            upper=pause()
    if x==3:
        print ("Level 3")
        lower=True
        while lower:
            print()
            print('please enter an element')
            answer=input()
            if answer in ComputerParts:
                print(answer," is in the array")
            else: print(answer, "is not in the array")
            lower=pause() 
    if x==4:
        print("Level 4")
        if x == "Find":
            print("select an element 0:5")
            y = int(input())
            print(ComputerParts[y])
            break
        if x =="Index":
            print("what items index would you like?")
            index=pause
            answer=input()
            index = ComputerParts.index(answer)
            print(answer, index)
            break
    if x==5:
        print("Level 5")
        split=True
        while split:
            print()
            answer=input()
            print('please enter a phrase')
            ComputerParts.reverse
            answer=input()
            print(ComputerParts.reverse)
            split=pause()
    if x==6:
        print ("Exit Game")