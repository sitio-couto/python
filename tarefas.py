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

print(getMaxVal(countDict([1,2,3,3,3,2,1,3,2,2,2,2,2])))
