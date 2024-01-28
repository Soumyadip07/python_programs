def get_user_input():
    n = int(input("Enter the number of transactions:" ))
    #DONE BY SOUMYADIP TIKADER
    data = []
    for i in range(n):
        items = input(f"Enter Transaction no. {i+1} items: ")
        fff=items.split()
        data.append([i,fff])
        #DONE BY SOUMYADIP TIKADER
    return data
data = get_user_input()
#DONE BY SOUMYADIP TIKADER
init = []
for i in data:
    for q in i[1]:
        if(q not in init):
            init.append(q)
            #DONE BY SOUMYADIP TIKADER
init = sorted(init)
support_percentage = float(input("Enter support threshold percentage: "))
#DONE BY SOUMYADIP TIKADER
s = round(float(support_percentage * len(init) / 100))
#DONE BY SOUMYADIP TIKADER
c = {}
for i in init:
    c[i] = 0
for i in init:
    #DONE BY SOUMYADIP TIKADER
    for d in data:
        if i in d[1]:
            c[i] += 1

print("C1:")
for i in c:
    print(str([i]) + ": " + str(c[i]))
print("\n        ===>")
#DONE BY SOUMYADIP TIKADER
l = {}
for i in c:
    if c[i] >= s:
        l[frozenset([i])] = c[i]
        #DONE BY SOUMYADIP TIKADER

print("F1:")
for i in l:
#DONE BY SOUMYADIP TIKADER
    print(str(list(i)) + ": " + str(l[i]))
print("--------------------")

pl = l
pos = 1
for count in range(2, 1000):
    nc = set()
    temp = list(pl)
    #DONE BY SOUMYADIP TIKADER
    for i in range(0, len(temp)):
        for j in range(i + 1, len(temp)):
            t = temp[i].union(temp[j])
            if len(t) == count:
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = {}
    for i in nc:
#DONE BY SOUMYADIP TIKADER
        c[i] = 0
        for q in data:
            temp = set(q[1])
            if i.issubset(temp):
                c[i] += 1

    print("C" + str(count) + ":")
    for i in c:
        print(str(list(i)) + ": " + str(c[i]))
        #DONE BY SOUMYADIP TIKADER
    print("        ===>")

    l = {}
    for i in c:
        if c[i] >= s:
            l[i] = c[i]

    print("F" + str(count) + ":")
    for i in l:
    #DONE BY SOUMYADIP TIKADER
        print(str(list(i)) + ": " + str(l[i]))
    print("---------------------")

    if len(l) == 0:
        break
    pl = l
    pos = count
#DONE BY SOUMYADIP TIKADER
print("Final Result we can consider as: ")
print("F" + str(pos) + ":")
for i in pl:
    print(str(list(i)) + ": " + str(pl[i]))
print()

from itertools import combinations
minimum_confidence =float(input("Enter minimum confidence: "))
#DONE BY SOUMYADIP TIKADER
for l in pl:
    c = [frozenset(q) for q in combinations(l,len(l)-1)]
    mmax = 0
    #DONE BY SOUMYADIP TIKADER
    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        #DONE BY SOUMYADIP TIKADER
        for q in data:
            temp = set(q[1])
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        temp = sab/sa*100
        if(temp > mmax):
            mmax = temp
        temp = sab/sb*100
        if(temp > mmax):
            #DONE BY SOUMYADIP TIKADER
            mmax = temp
        if((sab/sa*100)>minimum_confidence):
            print(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"% > "+str(minimum_confidence)+"%  ACCEPTED")
        if((sab/sb*100)<minimum_confidence):
            print(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"% < "+str(minimum_confidence)+"%  REJECTED")
        #DONE BY SOUMYADIP TIKADER
    curr = 1
    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in data:
        #DONE BY SOUMYADIP TIKADER
            temp = set(q[1])
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        #DONE BY SOUMYADIP TIKADER
        temp = sab/sa*100
        curr += 1
        temp = sab/sb*100
        #DONE BY SOUMYADIP TIKADER
        curr += 1
    print()