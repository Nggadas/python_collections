# MY SOLUTION
# def word_count(s):
#     s = s.lower()
#     list_s = s.split(' ')
#     dictionary = {}

#     for word in list_s:
#         count = list_s.count(word)
#         dictionary.update({word: count})

#     return dictionary



# print(word_count("I do not like it Sam I Am"))

# TREEHOUSE COMMUNITY SOLUTION
def word_count(a_str):
    a_dict = {}
    split_string = a_str.lower().split()

    for word in split_string:
        word_count = split_string.count(word)
        a_dict[word] = word_count

    return a_dict


print(word_count("I do not like it Sam I Am"))