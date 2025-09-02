from datetime import datetime, timedelta

now = datetime.now()
print(f"Current date and time: {now.strftime("%Y-%m-%d %H:%M:%S")}")
future = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {now.date() + timedelta(days=future)}")
