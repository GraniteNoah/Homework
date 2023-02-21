def lcm(a, b):
    if(a>b):
        if(a%b==0):
            return a

        else:
            total=a*b
            while(b!=0):
                temp=a%b
                a=b
                b=temp
            return total//a

    elif(a<b):
        if(b%a==0):
            return b

        else:
            total=b*a
            while(a!=0):
                temp=b%a
                b=a
                a=temp
            return total//b


    elif(a==b):
        return a

n=int(input())
i=0
nums=[]
while(i<n):
    nums=nums+[int(input())]
    i+=1

i=0
while(i<len(nums)):
    nums[0]=lcm(nums[0], nums[1])
    del nums[1]
    i+=1

print(nums[0])