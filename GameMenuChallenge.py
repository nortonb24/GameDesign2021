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
L10=('*      7.Exit                     *') 
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
    print('enter a selction 1-7')
    inputNumber = input()
    x=int(inputNumber)
    return x
L20=('***********************')
L21=('*       My Game       *')
L12=('*        Scores       *')
L13=('*      1.  5346       *')
L14=('*      2.  4323       *')
L15=('*      3.  4321       *')
L16=('*      4.  2343       *')
L17=('*      Exit game      *')
L18=('***********************')
def score():
    print(L20)
    print(L21)
    print(L12)
    print(L13)
    print(L14)
    print(L15)
    print(L16)
    print(L17)
    print(L18)
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
            print('please enter a phrase')
            answer=input()
            print(answer.capitalize())#is a method of string you have to refer with 
            capitalize=pause()
    if x==2:
        print ("Level 2")
        upper=True
        while upper:
            print()
            print('please enter a phrase')
            answer=input()
            print(answer.upper())#is a method of string you have to refer with 
            upper=pause()
    if x==3:
        print ("Level 3")
        lower=True
        while lower:
            print()
            print('please enter a phrase')
            answer=input()
            print(answer.lower())#is a method of string you have to refer with 
            lower=pause()
    if x==4:
        index=True
        while index:
            print()
            print('please enter a phrase')
            answer=input()
            print("Which character would you like to know the location of?")#is a method of string you have to refer with 
            again=input()
            completeINDEX= answer.index(again)
            print("The character is located at ",completeINDEX)
            index=pause()
    if x==5:
        split=True
        while split:
            print()
            print('please enter a phrase')
            answer=input()
            print(answer.split())#is a method of string you have to refer with 
            split=pause()
    if x==6:
        translate=True
        while translate:
            print()
            print('please enter a phrase')
            answer=input()
            change=answer.maketrans("a", "X")
            print(answer.translate(change))#is a method of string you have to refer with 
            translate=pause()
    if x==7:
        print ("Exit Game")