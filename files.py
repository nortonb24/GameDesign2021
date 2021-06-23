#Brenna Norton
#learn how to use files
import os
import sys
import time
#using time to pause your games

print ("HELLO")
time.sleep(2)
print ("there")
def readFile():
    file=input("what is the name of the file?")
    if os.path.exists(file): # to make sure the file exists
        #it opens the file 
        PEN=open(file, 'r')
        #prints the whole file 
        print(PEN.read())
    else:
        print('thank you')
fileName="BrennaNorton.txt"
if os.path.exists(fileName):
    print('Sorry that file exists')
else:
    FILE=open(fileName, 'w')
    FILE.write("************ THIS IS BRENNA NORTONS FILE ************")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.READ())
    FILE.close()
File=open("BrennaGame.txt", 'w')
newline="\n \n what ever"
File.write(newline)
File.close()
