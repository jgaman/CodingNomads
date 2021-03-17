'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount = int(input("Enter your investment amount:"))
interest_rate_in_percentage = float(input("Enter your interest rate in percentage:"))
number_of_years_to_invest = int(input("Enter the number of years to invest:"))
# FV=I×(1+(R×T))
future_values = (investment_amount * (1 + (interest_rate_in_percentage * number_of_years_to_invest)))
print("Your future values are:", round(future_values, 2))
