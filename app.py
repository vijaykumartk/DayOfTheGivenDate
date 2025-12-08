
month_lookup = {
    1: 13,
    2: 14,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12
}

day_lookup = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}

date = input ("Enter a date (DD/MM/YYYY): ")
day, month, year = map(int, date.split('-'))

if month in [1, 2]:
    year -= 1

q = int(day)
m = int(month_lookup[month])
k = int(year % 100)
j = int(year // 100)

day_of_week = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)

print("The day of the week is:", day_lookup[day_of_week % 7])

