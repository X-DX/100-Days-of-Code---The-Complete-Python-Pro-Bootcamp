# Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(2**3)

# Implicit Type Conversion in Python
# converts the datatype into another datatype automatically. Users don’t have to involve in this process.
c = 3 + 4.0
print(c)
print(type(c))

# Explicit Type Conversion in Python
# Python needs user involvement to convert the variable data type into the required data type.
# Mainly type casting can be done with these data type functions: int(), float(), str()
a = 4;
n = float(a)
print(n)
print(type(n))

# PEMDAS
# ()
# **
# *
# /
# +
# -

print("PEMDAS",3 * 3 + 3 / 3 - 3)
# print(9 + 1 - 3)
# print(10 - 3)
print(3 * (3 + 3) / 3 - 3)
