avg_speed = input("Enter average speed: ")
avg_speed = float(avg_speed)

# Set the distance
km_to_stockholm: int = 470

# Calculate the total travel time in minute
travel_time_mins_total = (km_to_stockholm / avg_speed) * 60

# Calculate the whole number of hours
travel_time_hours = travel_time_mins_total // 60

# Calculate the remainder in minutes
travel_time_mins_remain = travel_time_mins_total % 60

# Convert the values to integers
travel_time_hours = int(travel_time_hours)
travel_time_mins_remain = int(travel_time_mins_remain)

print("At an average speed of " + str(avg_speed) + " km/h it will take:")
print(str(travel_time_hours) + " hours and " + str(travel_time_mins_remain) + " minutes")
print("to travel the " + str(km_to_stockholm) + "km to Stockholm")