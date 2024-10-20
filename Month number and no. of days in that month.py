#month number and print number of days in that month
month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}
month_number = int(input("Enter month number (1-12): "))
if 1 <= month_number <= 12:
    print(f"Number of days: {month_days[month_number]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")