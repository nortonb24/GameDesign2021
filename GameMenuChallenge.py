#Brenna Norton
#I will be creating a game menu
#While loop
#Conditional if
#Function a piece of code that we will reuse
from typing import Text


L1=('***********************')
L2=('*       My Game       *')
L3=('*        Menu         *')
L4=('*      1.Level 1      *')
L5=('*      2.Level 2      *')
L6=('*      3.Level 3      *')
L7=('*      4.Level 4      *')
L8=('*      Exit game      *')
L9=('***********************')
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
    inputNumber = input()
    x=int(inputNumber)
    return x
L10=('***********************')
L11=('*       My Game       *')
L12=('*        Scores       *')
L13=('*      1.  5346       *')
L14=('*      2.  4323       *')
L15=('*      3.  4321       *')
L16=('*      4.  2343       *')
L17=('*      Exit game      *')
L18=('***********************')
def score():
    print(L10)
    print(L11)
    print(L12)
    print(L13)
    print(L14)
    print(L15)
    print(L16)
    print(L17)
    print(L18)
x=1
print ('hello')
print ('Goodbye')
while x !=4: #loop is conditioned to an event 
    x=menu() #expecting a return value
    if x==1:
        print("Level 1")
        print("give me a phrase")
        answer=input()
        upper=answer.capitalize()
        print(upper)
    if x==2:
        print ("Level 2")
    if x==3:
        print ("Level 3")
    if x==4:
        print ("Level 4")
    if x==5:
        print ("Exit Game")
print("Hi I am Brenna")
lower=answer.casefold()
print(lower)
        