#Brenna Norton
#06/11/2021
#Word Game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word
import datetime
import os 
import time
import random  
import sys 
os.system('cls')
#global vaiables
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
name=" "
dt=datetime.datetime.now()
score=0 #will total the amount of wins
#file="BrennaGame.txt" 
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A") 
def menu (): #to create a menu and define it
    print("*"*28) 
    print("*"," "*3,"Choice 1 - Play"," "*4,"*") 
    print("*"," "*3,"Choice 2 = Scores"," "*2,"*") 
    print("*"," "*3," 3 = Change Player"," "*1,"*") 
    print("*"," "*3,"Choice 4 = Exit"," "*4,"*") 
    print("*"*28) 
    #1 PLay game 
    #2 print score board 
    #3change player 
    #Exit 
    return input("What is your choice? ") 
def updateWord(word, guesses):  # function with a parameter to update word 
    for char in word: 
        if char in guesses: 
            print(char,end=' ') 
        else: 
            print('_', end =' ') 
def printScore(): 
    FileRead=open(file,'r') 
    print(FileRead.read()) 
    FileRead.close() 
    #Open file, count it as read and close file 
def updateScore(score): 
    FileWrite=open(file,'a') 
    line=name+"\t"+ linef+ "\t\t"+str(score) 
    FileWrite.write("\n"+ line) 
    FileWrite.close() 
    #will open the file and update the score 
    # date, name and,score 
#Start my main program 
def PlayGame(answer, score):    #My function in order to play game 
    while "Y" in answer: 
        os.system('cls') 
        print("Good luck ", name, "!") 
        word=random.choice(gameWords) 
        counter=len(word) 
        print(counter) 
        print (word)    #delete when we finish the code 
        turns= 10   #should we conider controlling this number when he/she misses 
        guesses='' 
        updateWord(word, guesses) 
        while turns>0 and counter >0: 
            newGuess=input("\n\n Give me a letter ") 
            #check that the new letter has not been used before 
            if newGuess not in guesses: 
                if newGuess not in word: 
                    turns -=1    #turns = turns -1 
                    print("Wrong! You have  ", turns, "guesses left") 
                else: 
                    counter -=word.count(newGuess) #deleten repeated letters 
                    print("nice guess!") 
                guesses += newGuess  
            else: 
                print("you used this one already") 
            updateWord(word, guesses) 
            #end of whole loop with  
        if counter==0: 
            #print("") 
            print("\n Fantastic you are Champion") 
            score +=1 
        else: 
            print("Sorry, try harder next time") 
        # find a way to decide if the person won the game or not  
        # keep a count of how many words they guessed    
        # #ask user if the want to play again 
        answer=input("Do you want to play again? ").upper() 
    updateScore(score) 
#your main Program 
check=True 
while check: 
    varChoice= menu() 
    if "1" in varChoice: 
        PlayGame("Y",score) 
    elif "2" in varChoice: 
        printScore() 
        input("press enter when done") 
        os.system('cls') 
    elif "3" in varChoice: 
        name=input("What is your name?") 
    else: 
        print("Thank you for playing!") 
        check=False 
    time.sleep(1)  