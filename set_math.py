COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers_all(arg):
    course_list = []
    for key, value in COURSES.items():
        if (value & arg) == arg:
            course_list.append(key)
    return course_list


print(covers_all({"conditions", "input"}))


def covers(arg):
    course_list = []
    for key, value in COURSES.items():
        if value & arg:
            course_list.append(key)
    return course_list