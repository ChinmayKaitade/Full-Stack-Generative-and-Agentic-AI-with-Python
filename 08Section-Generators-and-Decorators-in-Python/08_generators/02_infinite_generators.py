def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for __ in range(3):
    print(next(refill))
# Refill #1
# Refill #2
# Refill #3

for __ in range(5):
    print(next(user2))
# Refill #1
# Refill #2
# Refill #3
# Refill #4
# Refill #5

