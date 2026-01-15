flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        # print(f"{flavour} Item Found!")
        # Discontinued Item Found!
        # Out Side of Loop
        break
    print(f"{flavour} Item Found!")
    
print("Out Side of Loop")
# Ginger Item Found!
# Lemon Item Found!
# Out Side of Loop