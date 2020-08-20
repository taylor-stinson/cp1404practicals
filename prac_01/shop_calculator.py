"""
CP1404 Practical 1
Shop Calculator
"""

total_cost = 0
number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))
for i in range(0, number_items):
    item_cost = float(input("Price of item: $"))
    total_cost += item_cost
if total_cost > 100:
    total_cost = total_cost * 0.9
print("Total price for {} items is ${:.2f}".format(number_items, total_cost))

