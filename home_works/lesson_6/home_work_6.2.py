number = int(input("Enter your numbers: "))

DAY = 86400
HOUR = 3600
MINUTES = 60

days, suspension_second = divmod(number, DAY)
hours, suspension_second = divmod(suspension_second, HOUR)
minutes, seconds = divmod(suspension_second, MINUTES)

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

str_day = str()

if  1 < days % 10 < 5:
    if 10 < days < 15:
        str_day = "днів"
    else:
        str_day = "дні"
elif days % 10 == 1:
    if days == 11:
        str_day = "днів"
    else:
        str_day = "день"
else:
    str_day = "днів"


print(f"{days} {str_day}, {hours_str}:{minutes_str}:{seconds_str}")


