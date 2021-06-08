#Brenna Norton
#6/3/2021
# We are going to print a multiplication table for 2
#Using print statements 
#input --> variable is a container to keep data Neet and 
#They need to hava a valid and unique name
base=int(input)
print(type(base))
print("Multiplication Table of", base)
print()
for var in range (1,11):
    resolved= base*var
    print (base, 'x', var, '=', base*var)