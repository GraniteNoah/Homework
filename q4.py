
file = open ("grades.txt", "r")
text = file.read()
lines = text.splitlines()
data = {}
for line in lines:
    info = line.split()
    
    #stored as {id:{dept:{course:grade}}}
    if (info[2] not in data): data[info[2]] = {}
    if (info[0] not in data[info[2]]): data[info[2]][info[0]] = {}
    if (info[1] not in data[info[2]][info[0]]): data[info[2]][info[0]][info[1]] = info[3]
    #data stored

#menu
choice=input()
while (True):
    if (choice == "quit"):
        break
    ####################################
    elif (choice == "avg"):
        pot = input()
        pot.split()
        dept = pot[0]
        cn = pot[1]
        average = 0
        count = 0

        for i in data.values():
            for j in i.keys():
                if (j == dept):
                    for k in i.values:
                        for l in k.keys():
                            if (l == cn):
                                average += float(k[l])
                                count += 1
        average = average/count
        print("{:.2f}".format(average))
    ####################################
    elif (choice == "gpa"):
        sid = input()
        gp = 0
        count = 0
        for i in data[sid].values():
            for j in i.values():
                gp += float(j)
                count += 1
        gp = gp/count
        print ("{:.2f}".format(gp))
    ###################################
    elif (choice == "fails"):
        pot = input()
        pot.split()
        dept = pot[0]
        cn = pot[1]
        fails = 0

        for i in data.values():
            for j in i.keys():
                if (j == dept):
                    for k in i.values:
                        for l in k.keys():
                            if (l == cn):
                                if(int(k[l]) < 75):
                                    fails += 1
        print (fails)