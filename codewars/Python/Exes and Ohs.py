def xo(s):
    if len(s) == 0:
        return True
    s = s.lower()
    dic = dict()
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if dic['x'] == dic['o']:
        return True
    return False
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo("asdxoxo"))
