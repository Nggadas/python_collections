# return number of teachers
def stats(data_set):
    list = []

    for data in data_set:
        list.append([data, len(data_set[data])])

    return list

print(stats({'Andrew Chalkley': ['jQuery Basics', 'jQuery Basics'],
                    'Kenneth Love': ['Python Basics', 'Python Collections', 'Node.js Basics']}))

# return teacher with the most courses
def most_courses(data_set):
    max_count = 0
    teacher = ""

    for data in data_set:
        if len(data_set[data]) > max_count:
            max_count = len(data_set[data])
            teacher = data

    return teacher


# return number of teachers
def courses(data_set):
    courses = []

    for data in data_set:
        courses += data_set[data]

    return courses


# return number of teachers
def num_courses(data_set):
    count = 0

    for data in data_set:
        length = len(data_set[data])

        count += length

    return count


# return number of teachers
def num_teachers(data_set):
    count = 0

    for data in data_set:
        count += 1

    return count
