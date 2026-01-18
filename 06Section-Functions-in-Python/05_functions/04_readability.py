def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 15)
print(my_bill) # 45

print("Order for Table 2: ", calculate_bill(2, 50)) # Order for Table 2:  100