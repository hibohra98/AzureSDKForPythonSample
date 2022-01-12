# Implicit Type Conversion

"""
num_int = 123
num_float = 1.23

num_new = num_int + num_float

print("datatype of num_int:", type(num_int))
print("datatype of num_float:", type(num_float))


print("value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

"""


# Explicit Type Conversion
"""
num_int = 123
num_str = "543"

print("datatype of num_int:", type(num_int))
print("datatype of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("datatype of num_str after Type Casting:", type(num_str))

num_sum = num_str + num_int

print("sum of num_str and num_int:", num_sum)
print("Datatype of the sum:", type(num_sum))

"""


# Indentation
"""
color = "red"
if color == "green":
    print("Green Color")
else:
    if color == "blue":
        print("blue")
    else:
        for i in range(5):
            print(color)
"""