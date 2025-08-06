x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")


# Falsy: "", 0, None
# True: Everything else

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(""))
print(bool("False"))
