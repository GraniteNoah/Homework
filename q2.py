#get numbers
def getnum(order):
    print("Enter the", order,"number in the interval of [0, 100]:\n")
    x=int(input())
    return x

def checknums(x, y):
    if (x<0 or x>100):
        print("Magic Calculator cannot perform your operation!")
        return False
    else:
        return True

##main
print("Hi, how many operations do you want MagiCal to perform?")
numO=int(input())
i=0

while i<numO:
    print("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")
    choice=int(input())
    if (1<=choice and choice<=4):
        n1=getnum("first")
        n2=getnum("second")
        check=checknums(n1, n2)
        if (check==True):
            if (choice==1):
                result=n1+n2
                print(n1, "+", n2, "=", result, "\n")
            elif(choice==2):
                result=n1-n2
                print(n1, "-", n2, "=", result, "\n")
            elif(choice==3):
                result=n1*n2
                print(n1, "*", n2, "=", result, "\n")
            elif(choice==4):
                if(n2==0):
                    print("The denominator cannot be 0.\n")
                else:
                    result=n1/n2
                    print(n1, "/", n2, "=", result, "\n")

    else:
        print("Invalid input!\n")
    i+=1