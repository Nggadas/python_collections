def word_count(text):
    dictionary = {}
    text_to_lower = text.lower()
    split_text = text_to_lower.split()
    for word in split_text:
        count = split_text.count(word)
        dictionary[word] = count

    return dictionary


print(word_count("I do not like it Sam I Am"))
