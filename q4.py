def price(p):
    if (p%2!=0 and p%3!=0):
        a=p-1
        count=0
        while(a>0):
            if (a%2!=0 and a%3!=0):
                count+=1
            a-=1
        ##discount
        a=count-1
        while(a>0):
            if (a%2!=0 and a%3!=0):
                count-=1
            a-=1

    
    if (p%2==0 or p%3==0):
        a=p-1
        count=0
        while(a>0):
            if (a%2!=0 and a%3!=0):
                if (p%a==0):
                    count+=1
            a-=1
        ##discount
        a=count-1
        while(a>0):
            if (a%2!=0 and a%3!=0):
                if (count%a==0):
                    count-=1

    return count 


##main
n=int(input())
i=0
prices={}
while (i<n):
    prices[i]=price(int(input()))
    i+=1

sum=0
i=0
while(i<len(prices)):
    sum+=prices[i]
    i+=1

print(sum)