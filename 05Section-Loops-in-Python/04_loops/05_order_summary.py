names = ["Chinmay", "John", "Sam", "James"]
bills =[50, 70, 100, 40]

for names, amount in zip(names, bills):
    print(f"{names} paid ₹{amount} rupees")
# Chinmay paid ₹50 rupees
# John paid ₹70 rupees
# Sam paid ₹100 rupees
# James paid ₹40 rupees