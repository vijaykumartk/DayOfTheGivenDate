from resource.get_day_of_the_week import validate_date, calculate_day_of_week

def get_date_info():
    date = input ("Enter a date (DD/MM/YYYY): ")
    day, month, year = map(int, date.split('/'))

    if month in [1, 2]:
        year -= 1
    return day, month, year

if __name__ == "__main__":
    day, month, year = get_date_info()
    
    if not validate_date(day, month, year):
        print("Invalid date. Please enter a valid date in DD/MM/YYYY format.")
    else:
        day_of_week = calculate_day_of_week(day, month, year)
        print(f"The day of the week is: {day_of_week}")  
        

