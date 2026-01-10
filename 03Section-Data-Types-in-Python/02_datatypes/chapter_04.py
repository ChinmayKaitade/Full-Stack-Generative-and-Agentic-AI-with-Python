is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # upcasting
print(f"Total Actions: {total_actions}")

milk_present = 0 # no milk
milk_present = 11 # no milk --> True
milk_present = "hitesh" # no milk --> True
milk_present = 0 # no milk --> False
print(f"Is there Milk? {bool(milk_present)}")


water_hot = True
total_added = True
can_serve = water_hot and total_added
print(f"Can you serve Chai? {can_serve}")


