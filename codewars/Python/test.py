def count_smileys(arr):
    eyes = [":", ";"]
    nose = ["-", "~"]
    smil = [")", "D"]
    valid = 0
    for i in arr:
        if i[0] in eyes:
            if i[1] in nose or i[1] in smil:
                if len(i) !=2:
                    if i[2] in smil:
                        valid += 1
                else:
                    valid += 1  
    return valid