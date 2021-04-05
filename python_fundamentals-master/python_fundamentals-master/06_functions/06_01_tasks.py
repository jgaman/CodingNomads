"""

Write a script that completes the following tasks.

"""

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
user_input = int(input("Enter your number there:"))
def num_divisible_by_4_7 (user_input):
    if user_input % 4 == 0:
        return f"{user_input} is divisible by 4"
    elif user_input % 7 == 0:
        return f"{user_input} is divisible by 7"
    else:
        return "Your number is not divisible by 4 or 7"


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
