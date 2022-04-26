```python
def alphabet_position(text):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    result = ""
    for char in text:
        if char in alphabets:
            result += str(alphabets.index(char) + 1) + " "
    return result.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))
```