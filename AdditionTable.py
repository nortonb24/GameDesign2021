#Brenna Norton
#6/6/2021
# We are going to print an addition table
#Using print statements 
#input --> variable is a container to keep data neat and 
#They need to hava a valid and unique name
def main ():
    for y in range(0,13):

        for x in range(0,13):

            toWrite=""

            if y == 0:
                if x== 0:
                    toWrite= "+ "
                else:
                    toWrite= "{0} ".format(x)
            else:
                if x== 0: 
                    toWrite= "{0} ".format(y)
                else:
                    toWrite= "{0}".format(x+y)
            print ( toWrite.ljust(4, " "), end= '' ) # print without new line
        print ("") # print new line

