def filter_brackets(txt: str) -> str:
    brackets = ["[", "]", ","]
    special = ["'", '"']
    new_original = ""
    sp = 0
    print(txt)
    for i in str(txt):
        if i in brackets and sp == 0 :
            new_original += i
        else:
            if i in special:
                sp += 1
                if sp == 2 :
                    sp = 0
    return new_original

def same_structure_as(original, other):
    original = filter_brackets(original)
    other = filter_brackets(other)
    for i, v in enumerate(original):
        try:
            if v != other[i]:
                return False
        except:
            return False
    return True

# structure = lambda v: map(structure, v) if type(v) == list else ()
# same_structure_as = lambda a, b: structure(a) == structure(b)

# def same_structure_as(a, b):
#     return type(a) == type(b) and ( len(a) == len(b) and all(map(same_structure_as, a, b)) ) if type(a) == list else 1

print(same_structure_as([1, '[', ']'], ['[',']',1]))
