chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order: {chai_order}") # Chai Order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}

chai_recipe = {}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"

print(f"Recipe Base: {chai_recipe['base']}") # Recipe Base: black tea
print(f"Recipe Base: {chai_recipe}") # Recipe Base: {'base': 'black tea', 'liquid': 'milk'}
del chai_recipe['liquid']
print(f"Recipe Base: {chai_recipe}") # Recipe Base: {'base': 'black tea'}

print(f"Is Sugar is the Order? {'sugar' in chai_order}") # Is Sugar is the Order? True

chai_order = {"type":"Ginger Chai", "size":"Medium", "sugar":1}

print(f"Order Details (keys): {chai_order.keys()}") # Order Details (keys): dict_keys(['type', 'size', 'sugar'])
print(f"Order Details (values): {chai_order.values()}") # Order Details (keys): dict_keys(['type', 'size', 'sugar'])
print(f"Order Details (items): {chai_order.items()}") # Order Details (items): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)])


last_items = chai_order.popitem()
print(f"Removed Last Item: {last_items}") # Removed Last Item: ('sugar', 1)

extra_spices = {"cardamom":"crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai Recipe: {chai_recipe}") # Updated Chai Recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

chai_size = chai_order["size"]
print(f"Chai Size is: {chai_size}") # Chai Size is: Medium 

customer_note = chai_order.get("note", "No Note")
print(f"Customer Note is: {customer_note}") # Customer Note is: No Note



