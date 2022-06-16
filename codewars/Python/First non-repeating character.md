```python
def first_non_repeating_letter(string):
    string_lower = [x for x in string.lower()]
    for i in range(len(string_lower)):
        if string_lower.count(string_lower[i]) == 1:
            return string[i]
    return ''

print(first_non_repeating_letter("Dimas"))
```