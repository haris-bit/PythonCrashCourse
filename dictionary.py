weekConversion = {
    0: "Monday",
    1: "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
}

#print(weekConversion["Sun"])

print(weekConversion.get(0, "An invalid key"))