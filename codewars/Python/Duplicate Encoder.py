def duplicate_encode(word):
    word = word.lower()
    emote_word = ""
    for letter in word:
        if word.count(letter) > 1:
            emote_word += ")"
        else:
            emote_word += "("
    return emote_word
    
print(duplicate_encode("dragon noid is the best"))