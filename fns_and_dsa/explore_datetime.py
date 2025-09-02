from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
    future_date = int(input("Enter the number of days to add to the current date: "))
    print(f"Future date: {current_date.date() + timedelta(days=future_date) }")

display_current_datetime()
