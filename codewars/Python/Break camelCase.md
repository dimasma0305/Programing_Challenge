```python
def solution(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = ""
    # if one of upper case in s
    for i in s:
        if i in upper:
            word += " "+i
        else:
            word += i
    return word

print(solution("3people unFollowed me"))
```