numbers = [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]
index = 1

for number in numbers[1::2]:
    numbers[index] = number + 1
    index += 2

print(numbers)



