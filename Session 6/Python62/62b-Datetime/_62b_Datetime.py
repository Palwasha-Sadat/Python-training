import datetime

# Get the current date and time
todayWithTime = datetime.datetime.now()

# Print the current date and time
print(todayWithTime)

# Format and print the current time
print("The current time is", todayWithTime.strftime("%H:%M:%S"))

# Get the day of the week (0 = Monday, 6 = Sunday)
day_of_week = todayWithTime.weekday()

# Print the day of the week
print("The day of the week is:", day_of_week)
