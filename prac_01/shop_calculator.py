"""
DISCOUNT = 0.9
total_price = 0
get number_of_item
while number_of_item < 0
    display error message
    get number_of_item

for i in range(number_of_item)
    get price_per_item
    total_price = total_price + price_per_item

if total_price > 100
    total_price = total_price * DISCOUNT

display number_of_item and total_price
"""
DISCOUNT = 0.9 #10%
total_price = 0
number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    price_per_item = float(input("Price of item: "))
    total_price += price_per_item

if total_price > 100:
    total_price *= DISCOUNT

print(f"Total price for {number_of_item} items is ${total_price:.2f}")