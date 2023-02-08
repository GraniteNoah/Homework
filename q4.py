

##main
print("What is the height of the pyramid?\n")
h = int(input())
i = 1
width = 16
track = ''

if (1 < h and h < 10):
    while (i<=h):
        print (end=" " * width)
        width -= 2
        if (i==1):
            print("1")
        if (i == 2):
            print ("1 2 1")
        if (i == 3):
            print ("1 2 3 2 1")
        if (i == 4):
            print ("1 2 3 4 3 2 1")
        if (i == 5):
            print ("1 2 3 4 5 4 3 2 1")
        if (i == 6):
            print ("1 2 3 4 5 6 5 4 3 2 1")
        if (i == 7):
            print ("1 2 3 4 5 6 7 6 5 4 3 2 1")
        if (i == 8):
            print ("1 2 3 4 5 6 7 8 7 6 5 4 3 2 1")
        if (i == 9):
            print ("1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1")
        i+=1

else:
    print("PyNum cannot help you!")