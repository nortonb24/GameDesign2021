#Brenna Norton
#6/3/2021
# We are going to print a multiplication table for 2
#Using print statements 
#input --> variable is a container to keep data Neet and 
#They need to hava a valid and unique name 
base=2
var2=7
print (1*base)
print (2*base)
print (3*base)
print (4*base)
print (5*base)
print (6*base)
print (7*base)
print (8*base)
print (9*base)
print (10*base)
#repetition I should think of looping exact for statement 
for i in range (1,11): #begining of range is included end of range is not 
    print (i*base, end= "   ")
base=3
print ()
for i in range (1,11): #begining of range is included end of range is not 
    print (i*base, end= "   ")
    base=4
print ()
for i in range (1,11): #begining of range is included end of range is not 
    print (i*base, end= "   ")
    #when we have several repetition then we can use several loops
    #sometimes they can be nested loops
print()
for var in range (2,11):
    for i in range (1,11):
        print (i*var, end= "   ")
    print ()