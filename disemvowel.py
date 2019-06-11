def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = list(word)

    for letter in word:
        if letter.lower() in vowels:
            letters.remove(letter)

    return ''.join(letters)

print(disemvowel("alicktish"))