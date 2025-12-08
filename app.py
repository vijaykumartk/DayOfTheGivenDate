
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

def get_date_info():
    date = input ("Enter a date (DD/MM/YYYY): ")
    day, month, year = map(int, date.split('/'))

    if month in [1, 2]:
        year -= 1
    return day, month, year

def validate_date(day, month, year):
    if month < 1 or month > 12:
        return False
    
    if day < 1 or day > 31:
        return False
    
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
            
    if month in [4, 6, 9, 11] and day > 30:
        return False
    return True

def calculate_day_of_week(day, month, year):
    q = day
    m = month_lookup[month]
    k = year % 100
    j = year // 100
    day_of_week = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)
    return day_of_week

def print_day_of_week(day_of_week):
    print("The day of the week is:", day_lookup[day_of_week % 7])


if __name__ == "__main__":
    day, month, year = get_date_info()
    
    if not validate_date(day, month, year):
        print("Invalid date. Please enter a valid date in DD/MM/YYYY format.")
    else:
        day_of_week = calculate_day_of_week(day, month, year)
        print_day_of_week(day_of_week)

