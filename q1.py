n=int(input())
i=0
set1={}
while(i<n):
    set1[i]=input()
    i+=1

set2={}
j=0
while(j<len(set1)):
    temp=""
    i=0
    while (i<len(set1[j])):
        if (ord(set1[j][i])>=97 and ord(set1[j][i])<=122):
            temp+=chr(ord(set1[j][i])-32)
        elif (set1[j][i]!=" " and set1[j][i]!=","):
            temp+=set1[j][i]
        i+=1
    set2[j]=temp
    j+=1


for key in set2:
    temp=0
    for l in set2[key]:
        temp+=ord(l)
    set1[key]=temp

set3={}
for x in set1:
    if set1[x] not in set3:
        set3[set1[x]]=1
    else:
        set3[set1[x]]+=1


temp=0
for x in set3:
    if (set3[x]>temp):
        temp=set3[x]

print(temp)