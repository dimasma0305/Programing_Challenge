# def decode(s):
#     print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
#     print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
#     print(encode("!@#$%^&*()_+-"))
#     a,b,c = "", "", ""
#     for w in "abcdefghijklmnopqrstuvwxyz":
#         a += encode(  "" + w)[0]
#         b += encode( "_" + w)[1]
#         c += encode("__" + w)[2]
#     print(a)
#     print(b)
#     print(c)
#     return s;

# test.assert_equals(decode("atC5kcOuKAr!"), "Hello World!")

from z3 import *

txt = "Hello World"
dec = "atC5kcOuKAr"

txts = Ints(i for i in txt)
decs = Ints(i for i in dec)


s = Solver()
s.add([txts[i] == ord(v) for i, v in enumerate(txt)])
print(s)