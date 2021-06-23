#Brenna Norton
#We are going to learn how to read files per line
#How to make a list from a file
#And manipulate an element to find what you need 
import datetime
import os 
import time
import random  
import sys 
file=("test.txt")
FILE= open(file, 'r')
content= FILE.read() #is a string with full content of the file
print(content)
FILE.close()
FILE= open(file, 'r')
content_List=FILE.readlines()
print(content_List)
FILE.close()
for element in content_List:
    print("line: ", element)
    elem_list=element.split()
    print(elem_list)
    time.sleep(1)


#How do we reorder our score file by highest to lowest score 