import string
def accum(s):
    n = list()
    for i, c in enumerate(s):
        n += [c*(i+1)]
    return "-".join([string.capwords(i) for i in n])


print(accum("abc"))
