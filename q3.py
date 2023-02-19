source=input()

remove = ", "
new = ""

for each in source:
    if each not in remove:
        new += each

source=new

f=len(source)-1
i=0
Flag=0

while(i<f):
    Flag=-1
    if(source[i]==source[f] or ord(source[i])==ord(source[f])+32 
    or ord(source[i])==ord(source[f])-32):
        Flag=1
    i+=1
    f-=1

if (Flag==1):
    print ("Yes")

elif (Flag==-1):
    print ("No")