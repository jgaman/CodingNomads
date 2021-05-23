"""

Write a script that completes the following tasks.

"""

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

user_input = input("Enter your number there to see if it divisible by 4 and 7: ")
int_user_num = int(user_input)


def div_by_4_7(num):
    print("It's", num % 4 == 0 and num % 7 == 0, "that", user_input, "is divisible by 4 and 7")


div_by_4_7(int_user_num)

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
