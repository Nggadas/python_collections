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


def covers(topics):
    courses = []
    for course_title, topics_list in COURSES.items():
        if topics.intersection(topics_list):
            courses.append(course_title)

    return courses


def covers_all(topics):
    courses = []
    for course_title, topics_list in COURSES.items():
        if topics.issubset(topics_list):
            courses.append(course_title)

    return courses


print(covers_all({"conditions", "input"}))
