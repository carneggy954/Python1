# Prompt the user to enter time in hours
hours = float(input("Enter time in hours: "))

# Convert hours to minutes and seconds
minutes = hours * 60
seconds = hours * 3600

# Display the results
print("Time in minutes:", minutes)
print("Time in seconds:", seconds)