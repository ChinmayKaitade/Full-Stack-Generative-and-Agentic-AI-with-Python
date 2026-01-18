menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai",
]

# iced_tea = [my_tea for my_tea in menu if len(my_tea) > 10]

# print(iced_tea) # ['Masala Chai', 'Iced Lemon Tea', 'Iced Peach Tea', 'Ginger Chai']

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea) # ['Iced Lemon Tea', 'Iced Peach Tea']



