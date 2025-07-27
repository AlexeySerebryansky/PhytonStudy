number = 224930

time = {
    "day" : 86400,
    "hour" : 3600,
    "minutes" : 60
}


day = number//time["day"]
hour = (number - (time["day"] * 2)) // time["hour"]
minutes = ((number - (number//time["day"])) - (number - (time["day"] * 2)) // time["hour"]) // time["minutes"]



print(day, "days, ", hour, ":", minutes )
