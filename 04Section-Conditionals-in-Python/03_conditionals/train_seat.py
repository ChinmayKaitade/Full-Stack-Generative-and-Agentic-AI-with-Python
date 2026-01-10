seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, Beds available")
    case "ac":
        print("AC - Air Conditioned, Comfy Ride")
    case "general":
        print("General - Cheapest Option, No Reservation")
    case "luxury":
        print("Luxury - Premium Seats with Meals")
    case _:
        print("Invalid Seat Type")

