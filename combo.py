def combo(first, second):
    output = []
    for index, value in enumerate(first):
        output.append((value, second[index]))

    return output


print(combo([1, 2, 3], 'abc'))
