"""

Write a script that completes the following tasks.

"""

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

user_input = input("Enter your number there: ")


def div_by_4_7(num):
    print(num % 4 == 0 and num % 7 == 0)


div_by_4_7(user_input)


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
