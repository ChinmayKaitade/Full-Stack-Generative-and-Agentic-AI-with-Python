essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}") # All Spices: {'ginger', 'cardamom', 'cinnamon', 'cloves', 'black pepper'}

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}") # Common Spices: {'ginger'}

only_in_essential = essential_spices - optional_spices
print(f"Only in Essential Spices: {only_in_essential}") # Only in Essential Spices: {'cardamom', 'cinnamon'}

print(f"Is Cloves in Optional Spices: {'cloves' in optional_spices}") # Is Cloves in Optional Spices: True





