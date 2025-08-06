# Everything on python is object

course = "  python programming language "
print(course.upper())  # Do not change the value of the variable
print(course)


print(course.title())
print(course.strip())
print(course.lstrip())

print(course.find("pro"))
print(course.find("Pro"))  # it is capital sensitive so it will print -1
print(course.replace("p", "j"))
print("pro" in course)
print("Pro" in course)  # it will print false, because it is case sensitive
print("swift" not in course)
