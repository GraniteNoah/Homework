def take_int():
    print("Enter a positive integer:\n")
    x=int(input())
    if(x<0):
        print("PrimeFinder ignores negative numbers!")
        return -1
    elif(x>=0):
        return x

##main
print("How many numbers do you want to check?\n")
n = int(input())
i = 0
count = 0
while(i<n):
    prime=True
    num = take_int()
    
    if(num == -1):
        i-=1

    else:
        if(num % 2 == 0):
            prime = False

        elif(num % 3 == 0):
            prime = False

        if(prime == True):
            print(num, "is a prime number.\n")
            count += 1

    i += 1

print("Total prime numbers:", count)