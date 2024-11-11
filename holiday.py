# Start
# Calculate a user's total holiday cost
# Include plane, hotel and car rental cost
# Ask user to input destination, number of nights and number of days car rental
# Create four functions: hotel_cost(), plane_cost(), car_rental() and holiday_cost()
# Print all details in plain English
# End


# Ask user to input destination, number of nights and number of car rental days
# Require integers for nights and car rentals 

def flight_choices():
    print("Paris")
    print("New York")
    print("Sydney")
print("Please choose your flight destination.")
flight_choices()
city_flight = input("Please enter your destination: ")

num_nights = int(input("How many nights will you be staying at the hotel? "))
rental_days = int(input("How many days are you hiring a car for? "))


# Function to calculate hotel cost using num_flights as argument

def hotel_cost(num_nights):
    return num_nights * 210

print("The total cost of the hotel stay is £", hotel_cost(num_nights))


# Function to calculate plane cost using city_flight and if/else statements

def plane_cost(city_flight):
    if city_flight == "Sydney":
        return 860
    elif city_flight == "New York":
        return 545
    elif city_flight == "Paris":
        return 144
    else:
        print("Destination unknown.")

print ("The return cost of a flight to", city_flight, "is £", plane_cost(city_flight))


# Function to calculate car rental cost

def car_rental(rental_days):
    return rental_days * 25

print("The total cost of the car rental is £", car_rental(rental_days))


# Function to take three arguments num_nights, city_flight, rental_days
# Call three functions above with respective arguments
# Return total holiday cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print("The total cost of your holiday is £", holiday_cost(hotel_cost, plane_cost, car_rental))