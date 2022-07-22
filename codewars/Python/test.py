def are_you_playing_banjo(name):
    print(name[0].lower() == "r")
    return (name+" does not play banjo" if name[0].lower() != "r" else name+" plays banjo")

print(are_you_playing_banjo("ringo"))