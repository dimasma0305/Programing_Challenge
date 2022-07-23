def open_or_senior(data: list):
    return ["Senior" if j[0] >= 55 and j[1] > 7 else "Open" for j in data]

print(open_or_senior([(74, 10), (55, 6), (12, -2), (68, 7)]))