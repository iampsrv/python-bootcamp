import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current datetime:", current_datetime)

# Get the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Create a specific date
specific_date = datetime.date(2024, 2, 27)
print("Specific date:", specific_date)

# Format a date as a string
formatted_date = specific_date.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

# Parse a string into a datetime object
date_string = "2024-02-27"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date:", parsed_date)

# Calculate the difference between two dates
date1 = datetime.date(2024, 2, 27)
date2 = datetime.date(2024, 3, 5)
difference = date2 - date1
print("Difference in days:", difference.days)
