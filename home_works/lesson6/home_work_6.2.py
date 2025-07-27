number = 224930

DAY = 86400
HOUR = 3600
MINUTES = 60

days, suspension_second = divmod(number, DAY)
hours, suspension_second = divmod(suspension_second, HOUR)
minutes, seconds = divmod(suspension_second, MINUTES)

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(days, "days,", f"{hours_str}:{minutes_str}:{seconds_str}")


