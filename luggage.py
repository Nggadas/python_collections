def packer(**kwargs):
    return kwargs


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


# print(packer(name="John", num=42, spanish_iniquisition=None))
# packed = packer(name="John", num=42, spanish_iniquisition=None)
# unpacker(**{"last_name": "Doe", "first_name": "John"})

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
