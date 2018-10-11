# from collections import Counter

def getEven(l):
    return [x for x in l if x%2 == 0]

def getEvenPos(l):
    return l[0::2]

def countDict(l):
    dic = {key : 0 for key in l}
    for i in l: dic[i] += 1
    return dic

# def countDict2(l):
#     return Counter(l)

def getMaxVal(d):
    return max(d, key=d.get)

def getMode(l):
    return getMaxVal(countDict(l))

def subList(l, s):
    return any ( l[i:len(s)+i]==s for i in range(len(l)) )

def intersect(a, b):
    return any ( a[i:]==b[:len(a)-i] for i in range(len(a)-len(b),len(a)))
