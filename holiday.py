# A program that calcualtes a users holiday cost including plane cost, 
# hotel cost, and car rental cost

# 2D Distionary containing different holiday options
holiday_options = {
    "London":{"hotel per night": 200, "flight cost": 100, "rental cost": 60},
    "Miami":{"hotel per night": 250, "flight cost": 800, "rental cost": 50},
    "Paris":{"hotel per night": 300, "flight cost": 1000, "rental cost": 40}
}

# Creates a list of locations from dictionary keys and concatinates into a string
destinations_str = ""
key_list = list(holiday_options.keys())
for key in range(len(holiday_options)):
    destinations_str += key_list[key] + ", "


# User inputs validated to be passed as arguements to functions later
input_valid = 0
while input_valid !=1:
    try:
        city_flight = input(
            f"Select one of the destinations: {destinations_str.strip(', ')}: ").capitalize()
        num_nights = int(input("How many nights will you stay? "))
        rental_days = int(input("How many days will you rent car? "))
        if holiday_options[city_flight] != None:
            input_valid = 1
    except:
        print("Ivalid input, Try again.")
        continue

print(holiday_options.get(city_flight))
# calculates total cost of hotel
def hotel_cost(nights):
    hotel_price = holiday_options[city_flight]["hotel per night"]
    price = nights * hotel_price
    return price


# calcuates cost of flight
def plane_cost(cost):
    cost = holiday_options[city_flight]["flight cost"]
    return cost


# calculates cost of car rental
def car_rental(days):
    cost = days * holiday_options[city_flight]["rental cost"]
    return cost


# calculates total cost of holiday and outputs information for user
def holiday_cost(num_nights, city_flight, rental_days):
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    rental_total = car_rental(rental_days)
    total_cost = hotel_total + plane_total + rental_total
    print("\n" * 3)
    print(f'''
You have selected to go to {city_flight} for {num_nights} nights and rent a car
for {rental_days} days. Below is a breakdown of your expenses.\n
''')
    print(f"Car rental cost: £{rental_total}")
    print(f"Plane Cost: £{plane_total}")
    print(f"Hotel cost: £{hotel_total}")
    print(f"\nTotal holiday cost: £{total_cost}")

holiday_cost(num_nights, city_flight, rental_days)