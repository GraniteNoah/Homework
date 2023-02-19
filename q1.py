


while(True):
    source = input()
    if(source == "quit"):
        break

    k = int(input())

    if (len(source) <= k):
        print(source)
    
    else:
        all = {}
        i=0
        j=0
        while(i<=len(source)-j):
            letters=""
            j=0
            while(j<k):
                letters = letters + source[i+j]
                all[i] = letters
                j+=1
            i += 1
        ans1 = {}
        i = 0
        while(i<len(all)):
            track = {}
            for j in all[i]:
                if (j not in track):
                    track[j] = 1
                else:
                    track[j] += 1
            ans1[i] = len(track)
            i+=1
        counter = k
        ##pinting error
        i=0
        Flag=True
        while (i<len(ans1) and Flag):
            for j in ans1:
                if ans1[j] == counter:
                    print(all[j])
                    Flag = False
                    break
            counter-=1    
                


