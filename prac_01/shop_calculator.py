tallied_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    cost_of_item = float(input("Price of item: "))
    tallied_cost = tallied_cost + cost_of_item
if tallied_cost > 100:
    total_cost = tallied_cost*0.9
else:
    total_cost = tallied_cost
print(f"Total price for {number_of_items} items is ${total_cost:.2f}" )