# import library for alphabet
import string

def high(x):
    alphabet = string.ascii_lowercase 
    dic = dict()
    sm = dict()
    alp = ""
    for i in range(len(x)):
        if x[i] in alphabet:
            if x[i] in dic:
                dic[x[i]] += ord(x[i]) - 96
                alp += x[i]
            else:
                dic[x[i]] = ord(x[i]) - 96
                alp += x[i]
        if x[i] == " ":
            sm[alp] = sum(dic.values())
            alp = ""
            dic = dict()
    sm[alp] = sum(dic.values())
    return max(sm, key=sm.get)

def high(x):
    print(x.split())
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

print(high("ab ac cd"))