from day_lookup import day_lookup
from month_lookup import month_lookup

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
    day_number_of_week = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7
    day_of_week = day_lookup[day_number_of_week]
    return day_of_week
    