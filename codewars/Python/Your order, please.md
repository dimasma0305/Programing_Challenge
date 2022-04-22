```python
def order(sentence):
    sentence = sentence.split()
    pointer = {}
    for i in range(len(sentence)):
        for j in range(len(sentence[i])):
            if sentence[i][j].isdigit():
                pointer[sentence[i][j]] = sentence[i]
    return " ".join([pointer[str(i)] for i in range(1, len(pointer)+1)])
            
print(order("is2 Thi1s T4est 3a"))
```