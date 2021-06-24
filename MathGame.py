#Brenna Norton
#6/22/2021
#My final project
#Goal-to create a math game with a menu 
from datetime import datetime
import os, sys, time, random, math
#Global Variables
file='MathGameScores.txt'
score=0
dt=datetime
#linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")
 
os.system('cls')
name= input("What is your name?")
print(name)
print("Good Luck", name,)

#to create and define a menu
L1= ("*************************************")
L2= ("*             Math Game             *")
L3= ("*               Menu                *")
L4= ("*     --------------------------    *")
L5= ("*      1. Level 1 Addition          *")
L6= ("*      2. Level 2 Subbtraction      *")
L7= ("*      3. Level 3 Multiplication    *")
L8= ("*      4. Level 4 Division          *")
L9= ("*      5. Scores                    *")
L10=("*      6. Exit                      *")
L11=("*************************************")
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
    print('Please Enter a selction 1-6')
    inputNumber=(int)(input())
    return inputNumber

#score function
def updateScore(score): 
    FileWrite=open(file,'a') 
    line=name+"\t"+ linef+ "\t\t"+str(score) 
    FileWrite.write("\n"+ line) 
    FileWrite.close() 
def printScore(): 
    FileRead=open(file,'r') 
    print(FileRead.read()) 
    FileRead.close()


digits= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,]

#to ask questions for each sign
def Question(operator):
    x = random.choice(digits)
    y = random.choice(digits)
    print("What is " + str(x) + operator +str(y))
    if "+" in operator:
        sum = x+y
    if "-" in operator:
        sum = x-y
    if "*" in operator:
        sum= x*y
    if "/" in operator:
        sum= x/y
    return sum

#addition function to play game
def addition():
    check=True
    turns = 5 
    score =0
    answer =0
    while check:
        operator= "  + "
        sum = Question(operator)
        answer=int(input())
        if sum == answer:
            print("You are so smart !!")
            score +=1
            turns -=1 #turns = turns -1
        else:
            print("Sorry you missed")
            turns -=1
        if turns== 0:
            check=False

 #subtraction function to play game           
def subtraction():
    check=True
    turns = 6
    score =0
    answer =0
    while check:
        operator= " - "
        sum = Question(operator)
        answer=int(input())
        if sum == answer:
            print("You are so smart !!")
            score +=1
            turns -=1
        else:
            print("Sorry you missed")
            turns -=1
        if turns== 0:
            check=False
            print("Your score is ", score)

#multiplication function to play game
def multiplication():
    check=True
    turns = 7
    score =0
    answer =0
    while check:
        operator= " * "
        sum = Question(operator)
        answer=int(input())
        if sum == answer:
            print("You are so smart !!")
            score +=1
            turns -=1
        else:
            print("Sorry you missed")
            turns -=1
        if turns== 0:
            check=False
            print("Your score is ", score)

#division function to play game
def division():
    check=True
    turns = 8
    score =0
    answer =0
    while check:
        operator= " / "
        sum = Question(operator)
        answer=int(input())
        if sum == answer:
            print("You are so smart !!")
            score +=1
            turns -=1
        else:
            print("Sorry you missed")
            turns -=1
        if turns== 0:
            check=False
            print("Your score is ", score)
          #update score file  
#creating function for each level
x=0
while x !=7: #loop is conditioned to an event 
    x=menu()
    if x==1: #Addition game
        print("Level 1 Selected")
        print(name,"Get ready...")
        time.sleep(1)
        print("Addition Game")
        time.sleep(1)
        addition()
        
        #Addition=True
    
    if x==2: #Subtraction Game
        print("Level 2 Selected")
        print(name, "Get ready...")
        time.sleep(1)
        print("Subtraction Game")
        time.sleep(1)
        subtraction()
    
        
    if x==3: #Multiplication Game
        print("Level 3 Selected")
        print(name, "Get ready...")
        time.sleep(1)
        print("Multiplication Game")
        time.sleep(1)
        multiplication()
    
    if x==4: #Division Game
        print("Level 4 Selected")
        print(name, "Get ready...")
        time.sleep(1)
        print("Division Game")
        time.sleep(1)
        division()
        
    if x==5: #scores
        printScore() 
        input("press enter when you are done viewing scores") 
    if x==6:
        print(name, "Thank you for playing!!")
        print("Goodbye:)")
        sys.exit()
    time.sleep(1)

