# naive date and time
# it doesn't know the timezone
# it just tells your computer time and date
from datetime import datetime, timezone, timedelta
date = datetime.now()
print(date)


# aware time zone
date = datetime.now(timezone.utc) # utc is the central point from where all time zone are meausered
print(date)



print()

######### adding time to current time
today = datetime.now(timezone.utc)
tommorow = today + timedelta(days=1)

print("today is", today)
print("tommorow is", tommorow)


print()



# string format time
print("today's formated time", today.strftime('%d-%m-%Y  %H:%M:%S'))
"""
d - date
m - month
Y - Year
H - hour
M - minutes
S - second
"""

print()



# string parse time, for taking input from the user
user_date = input("Enter your date in dd-mm-YYYY format: ") # default time will be taken as 00:00:00
user_date = datetime.strptime(user_date, "%d-%m-%Y")
print("user_date : ", user_date)

print()