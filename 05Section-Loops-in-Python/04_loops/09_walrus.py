# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
    # Not divisible, remainder is 3


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your Chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} Chai")
else:
    print(f"Size is available - {requested_size}")


flavors = ["masala", "ginger", "lemon", "mint"]
print("Available Flavors: ", flavors)


while (flavor := input("Choose your flavors: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
# Available Flavors:  ['masala', 'ginger', 'lemon', 'mint']
# Choose your flavors: masala
# You choose masala chai