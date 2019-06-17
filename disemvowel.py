def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = list(word)
    for letter in word.copy():
        if letter.lower() in vowels:
            word.remove(letter)

    return "".join(word)
