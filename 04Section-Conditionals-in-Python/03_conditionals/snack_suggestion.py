snack = input("Enter Your Preferred Snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, We Only Serve Cookies or Samosa with Tea")


print(f"User Said: {snack}")

