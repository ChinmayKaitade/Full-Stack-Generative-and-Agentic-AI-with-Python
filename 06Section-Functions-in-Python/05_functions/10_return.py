def make_chai():
    # return "Here is your masala chai"
    print("Here is your masala chai")

return_value = make_chai()

# print(return_value) # Here is your masala chai
print(return_value) # None

def idle_chaiwala():
    pass

print(idle_chaiwala()) # None

def sold_cups():
    return 120

total = sold_cups()
print(total) # 120

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, Chai Over!"
    return "Chai is Ready!"

print(chai_status(0)) # Sorry, Chai Over!
print(chai_status(5)) # Chai is Ready!

def chai_report():
    return 100, 20, 10 # sold, remaining, not paid

sold, remaining, not_paid = chai_report()
print("Sold:", sold) # Sold: 100
print("Remaining:", remaining) # Remaining: 20
print("Not Paid:", not_paid) # Not Paid: 10