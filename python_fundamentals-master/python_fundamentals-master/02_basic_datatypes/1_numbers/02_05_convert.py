'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
int_number = int(input("Enter your int number there:"))
int_to_float = float(int_number)
print("this is your number in float:", int_to_float)
float_to_int = float(input("Enter your float number there:"))
print("Your int number there:", int(float_to_int))
print("this is the division of your number:", int_to_float, "*", float_to_int, "=", int_to_float * float_to_int)
