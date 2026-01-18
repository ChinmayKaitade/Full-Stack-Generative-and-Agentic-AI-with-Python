favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai",
]

unique_chai = {chai for chai in favorite_chais}
# unique_chai = {chai for chai in favorite_chais if len(chai) < 8} 
print(unique_chai) # {'Elaichi Chai', 'Lemon Tea', 'Masala Chai', 'Green Tea'}

recipes = {
    "Masala Chai": ["Ginger", "Cardamom", "Clove"],
    "Elaichi Chai": ["Cardamom", "Milk"],
    "Spicy Chai": ["Ginger", "Black Pepper", "Clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices) # {'Black Pepper', 'Milk', 'Ginger', 'Clove', 'Cardamom'}