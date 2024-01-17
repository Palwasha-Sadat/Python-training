import datetime

# Get the current date and time
todayWithTime = datetime.datetime.now()  # This variable stores the current date and time.
todayWithoutTime = datetime.date.today()  # This variable stores the current date without the time.

# Print the current date and time
print(todayWithTime)  # This line prints the current date and time.
print(todayWithoutTime)  # This line prints the current date without the time.

# Print the current date and time in specific formats
print("The current date is", datetime.datetime.strftime(todayWithoutTime, "%m/%d/%Y"))  # This line prints the date without time in MM/DD/YYYY format.
print("The current time is", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))  # This line prints the time with time in HH:MM:SS format.
