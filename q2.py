
source = input()
target = input()

i = 0
index=-1

while(i<len(source)):
    j=0
    Flag = False

    if (target[j]==source[i]):
        while(j<len(target)):
            Flag=False
            if (target[j]==source[i+j]):
                Flag=True
            j+=1

    if (Flag==True):
        index=i
        break


    i+=1

print(index)