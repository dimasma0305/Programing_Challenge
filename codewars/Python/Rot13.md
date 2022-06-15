```python
def rot13(message):
    enc = []
    for i in message:
        if i.isalpha():
            if i.isupper():
                i = chr((ord(i) - ord("A") + 13) % 26 + ord("A"))
            else:
                i = chr((ord(i) - ord("a") + 13) % 26 + ord("a"))
        enc.append(i)
    return ''.join(enc)
    
print(rot13("test"))
```