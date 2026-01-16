from datetime import date, timedelta

print("The date today is: " + str(date.today()))
print("The date in 7 days is: " + str((date.today() + timedelta(days=7))))