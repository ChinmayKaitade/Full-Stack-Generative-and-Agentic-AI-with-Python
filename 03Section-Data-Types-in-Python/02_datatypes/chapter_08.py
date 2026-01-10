ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar")
print(f"Ingredients are: {ingredients}") # Ingredients are: ['water', 'milk', 'black tea', 'sugar']
ingredients.remove("water")
print(f"Ingredients are: {ingredients}") # Ingredients are: ['milk', 'black tea', 'sugar']

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients: {chai_ingredients}") # Chai Ingredients: ['water', 'milk', 'ginger', 'cardamom']

chai_ingredients.insert(2, "black tea")
print(f"Chai: {chai_ingredients}") # Chai: ['water', 'milk', 'black tea', 'ginger', 'cardamom'] 

last_added = chai_ingredients.pop()
print(f"Last Added: {chai_ingredients}") # Last Added: ['water', 'milk', 'black tea', 'ginger']

chai_ingredients.reverse()
print(f"Chai Reverse: {chai_ingredients}") # Chai: ['ginger', 'black tea', 'milk', 'water'] 
chai_ingredients.sort()
print(f"Chai Reverse: {chai_ingredients}") # Chai Reverse: ['black tea', 'ginger', 'milk', 'water']
print(f"Last Added: {chai_ingredients.reverse()}") # Last Added: ['water', 'milk', 'black tea', 'ginger']

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level is: {max(sugar_levels)}") # Maximum sugar level is: 5
print(f"Minimum sugar level is: {min(sugar_levels)}") # Minimum sugar level is: 1

#***********************************************************************#

base_liquid = ["water","milk"]
extra_flavour = ["ginger"]


full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}") # Liquid mix: ['water', 'milk', 'ginger']

strong_brew = ["black tea"] * 3
print(f"String brew: {strong_brew}") # String brew: ['black tea', 'black tea', 'black tea']

# raw_spice_data = ["CINNAMON"]
raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}") # Bytes: bytearray(b'CINNAMON')

raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}") # Bytes: bytearray(b'CARDMON')
