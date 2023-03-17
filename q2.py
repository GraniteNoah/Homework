n=int(input())
list1=[]
i=0
while (i<n):
    list1.append(int(input()))
    i+=1

list2=[]

i=0
while(i<n):
    if(i==n-1):
        list2.append(list1[i])
    
    elif (list1[i]>=0 and list1[i+1]>=0 or list1[i]<0 and list1[i+1]<0):
        list2.append(list1[i]+list1[i+1])
        i+=1
    else:
        list2.append(list1[i])
    i+=1


i=0
list3=[]
while(i<len(list2)):
    if(i==len(list2)-1):
        list3.append(list2[i])
    
    elif (list2[i]>=0 and list2[i+1]>=0 or list2[i]<0 and list2[i+1]<0):
        list3.append(list2[i]+list2[i+1])
        i+=1
    else:
        list3.append(list2[i])
    i+=1



i=0
list4=[]
while(i<len(list3)):
    if(i==len(list3)-1):
        list4.append(list3[i])
    
    elif (list3[i]>=0 and list3[i+1]>=0 or list3[i]<0 and list3[i+1]<0):
        list4.append(list3[i]+list3[i+1])
        i+=1
    else:
        list4.append(list3[i])
    i+=1


i=0
sum={}
while(i<len(list4)):
    sum[i]={}
    j=i
    temp=0
    while(j<len(list4)):
        temp+=list4[j]
        sum[i][j]=temp
        j+=1
        
    i+=1


max=sum[0][0]

for k in sum.values():
    for p in k.values():
        if(max<p):
            max=p

print(max)
