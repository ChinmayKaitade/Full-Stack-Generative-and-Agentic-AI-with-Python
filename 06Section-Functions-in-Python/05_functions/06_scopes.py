def serve_chai():
    chai_type = "Masala" # Local Scope
    print(f"Inside function: {chai_type}") # Inside function: Masala

chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}") # Outside function: Lemon

def chai_counter():
    chai_order = "Lemon" # Enclosing Scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:",chai_order) # Inner: Ginger
    print_order()
    print("Outer:",chai_order) # Outer: Lemon

chai_order = "Tulsi" # Global
chai_counter()
print("Global:",chai_order) # Global: Tulsi




