"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode:
get sales
while sales >= 0
    if sales < 1000
        bonus = (10/100) * sales
    else
        bonus = (15/100) * sales
    display bonus
    get sales
"""

sales = float(input("Enter sales: $ "))
while sales >= 0:
    if sales < 1000:
        bonus = (10/100) * sales
    else:
        bonus = (15/100) * sales
    print(f"Your bonus based on $ {sales} is $ {bonus}.")
    sales = float(input("Enter sales: $ "))
