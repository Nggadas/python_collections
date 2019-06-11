def combo(first, second):
    list = []
    for index, iterable1 in enumerate(first):
        list.append((iterable1, second[index]))

    return list


print(combo([1, 2, 3], 'abc'))


def stringcases(s):

    uppercase = s.upper()
    lowercase = s.lower()
    tilecased = s.title()
    reverse = s[::-1]

    return (uppercase, lowercase, tilecased, reverse)