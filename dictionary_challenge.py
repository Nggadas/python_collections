def num_teachers(tree_house):
    return len(tree_house)


def num_courses(tree_house):
    total = 0
    for value in tree_house.values():
        total += len(value)

    return total


def courses(tree_house):
    course_list = []
    for value in tree_house.values():
        for course in value:
            course_list.append(course)

    return course_list


def most_courses(tree_house):
    max_count = 0
    course_teacher = ""
    for name, subjects in tree_house.items():
        if len(subjects) > max_count:
            max_count = len(subjects)
            course_teacher = name

    return course_teacher


def stats(tree_house):
    list_of_lists = []
    for teacher, subjects in tree_house.items():
        list_of_lists.append([teacher, len(subjects)])

    return list_of_lists


print(stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}))