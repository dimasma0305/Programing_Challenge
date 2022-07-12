'''
# old method
def permutations(string):
    if len(string) ==  1: 
        return [string]
    string = [i for i in string]
    ls_perm = []
    # print(string)
    for i in string:
        # print(i)
        tmp = string.copy()
        tmp.remove(i)
        # print(tmp)
        for j in range(len(tmp)):
            print(tmp[j:]+tmp[:j])
            foo = i + ''.join(tmp[j:]+tmp[:j])
            # if foo not in ls_perm:
            ls_perm.append(foo)
    return ls_perm
'''


def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)
    return result

print(permutations('abcd'))