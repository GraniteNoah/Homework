source=input()
f=len(source)-1
i=0

while(i<f):
    Flag=False
    if(source[i]==source[f] or ord(source[i])==ord(source[f])+32 
    or ord(source[i])==ord(source[f])-32):
        Flag=True
    i+=1
    f-=1

if (Flag):
    print ("Yes")

else:
    print ("No")