# The string len() function returns the length of the string
# len(12345)

# Type
print(type("Hello"))
print(type(123))
print(type(1.23))
print(type(True))

# Type Conversion
print(type(int("123")))
print(type(int("12") + int("12")))
print(type(float("1.22")))

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))
