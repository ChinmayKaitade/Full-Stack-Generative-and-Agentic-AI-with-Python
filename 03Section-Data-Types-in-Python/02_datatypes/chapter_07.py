masala_spices = ("cinnamon", "cardamom", "clove", "ginger")

(spice1, spice2, spice3,spice4) = masala_spices 

print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}, {spice4}") # Main Masala Spices: cinnamon, cardamom, clove, ginger

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}") # Ratio is G:2 and C:1
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}") # Ratio is G:1 and C:2

# membership testing
print(f"Is Ginger in Masala Spices ? {'ginger' in masala_spices}") # Is Ginger in Masala Spices ? True

