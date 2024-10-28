def hotel_cost(nights):
    """Calculate the cost of staying at the hotel for a given number of nights."""
    return 140 * nights      
              
def plane_ride_cost(city): 
    """Return the cost of a plane ride to the specified city."""
    if city == "Charlotte":
        return 183 
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh": 
        return 222
    elif city == "Los Angeles": 
        return 475
    else:
        return "City not listed"

def rental_car_cost(days):
    """Calculate the rental car cost based on the number of days."""
    rent = 40 * days
    if days >= 7:
        rent -= 50
    elif days >= 3:
        rent -= 20
    return rent
 
def trip_cost(city, days, spending_money):
    """Calculate the total cost of the trip."""
    if isinstance(plane_ride_cost(city), str):
        return plane_ride_cost(city)  
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


print(trip_cost("Los Angeles", 5, 600))


