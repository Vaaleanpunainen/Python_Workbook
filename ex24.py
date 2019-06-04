# program reads a duration from the user as a number of days, hours, minutes, and seconds,
# then computes and displays the total number of seconds represented by thid duration

dur_days = int(input("Enter the number of days: "))
dur_hours = int(input("Enter the number of hours: "))
dur_min = int(input("Enter the number of minutes: "))
dur_sec = int(input("Enter the number of seconds: "))

total_seconds = dur_days*86400 + dur_hours*3600 + dur_min*60 + dur_sec

print("%s days, %s hours, %s minutes and %s seconds is equal to %s seconds." %(dur_days, dur_hours, dur_min, dur_sec, total_seconds))
