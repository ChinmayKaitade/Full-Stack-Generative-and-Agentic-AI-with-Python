chai = "Ginger Chai"

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai) # Preparing Ginger Chai``
print(chai) # Ginger Chai

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai) # [1, 42, 3]

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional --> # Darjeeling Yes Low
make_chai(tea="Green", sugar="Medium", milk="No") #keywords --> # Green No Medium

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients) # Ingredients ('Cinnamon', 'Cardamom')
    print("Extras", extras) # Extras {'sweetener': 'Honey', 'foam': 'Yes'}

special_chai("Cinnamon", "Cardamom", sweetener="Honey", foam="Yes")

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order() # ['Masala']
# chai_order() # ['Masala', 'Masala']

def chai_order(order=None):
    if order is None:
        order = []

chai_order() 
chai_order() 






