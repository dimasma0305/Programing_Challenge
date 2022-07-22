numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
for i, j in numbers.items():
    exec(f"def {j}(f=None): return {i} if f is None else int(f({i}))")
oprt = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "divided_by": "/",
}
for i, j in oprt.items():
    exec(f"def {i}(y): return lambda x: x {j} y")
print(seven(times(five())))