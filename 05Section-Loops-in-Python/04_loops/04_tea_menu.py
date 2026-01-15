menu = ["Green", "Lemon", "Spliced", "Mint"]

for m in menu:
    print(f"Menu Item is {m}")
# Menu Item is Green
# Menu Item is Lemon
# Menu Item is Spliced
# Menu Item is Mint

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} Chai")
# 1 : Green Chai
# 2 : Lemon Chai
# 3 : Spliced Chai
# 4 : Mint Chai