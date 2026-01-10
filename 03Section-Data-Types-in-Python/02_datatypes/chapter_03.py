# Integer

black_tea_grams = 14
ginger_grams = 3


total_grams = black_tea_grams + ginger_grams
print(f"Total Grams of Base Tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total Grams of Remaining Base Tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk Per Serving is {milk_per_serving}")


total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole Tea Bags Per Pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup= 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover Cardamom Pods: {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scale Flavour Strength: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total Tea Leaves Harvested: {total_tea_leaves_harvested}")
