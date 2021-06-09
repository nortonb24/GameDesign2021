#Brenna Norton
#I will be creating a game menu
#While loop
#Conditional if
#Function a piece of code that we will reuse
from typing import Text


L1=('***********************************')
L2=('*       My Game                   *')
L3=('*        Menu                     *')
L4=('*      1.capitalize               *')
L5=('*      2.uppercase                *')
L6=('*      3.Lowercase                *')
L7=('*      4.find the index of char   *')
L8=('*      5.split                    *')
L9=('*      6.translate                *')
L10=('*     7. Exit                    *') 
L11=('**********************************')
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
    print(L11)
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
def pause():
    print("Press enter to continue")
    input()
x=1
while x !=4: #loop is conditioned to an event 
    x=menu() #expecting a return value
    if x==1:
        capitalize=True
        while capitalize==True:
            print("Level 1")
            print("please enter a number 1-4")
            answer=input()
            print(answer.capitalize())#is a method of string you have to refer with 
            print('do you want to convert another string?')
            if (x==again):
                print("please enter another phrase")
                answer=input() #input is a function
                print(answer.capitalize())#is a method of string you have to refer with 
                answer=answer.capitalize() #update your variable to the change if you dont need original value
                print(answer)
                pause()
            if(x==enter)
    if x==2:
        print ("Level 2")
    if x==3:
        print ("Level 3")
    if x==4:
        print ("Level 4")
    if x==5:
        print ("Exit Game")
