from resource.get_day_of_the_week import validate_date, calculate_day_of_week
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
async def greet():
    return "Hello world!"

@app.get("/calculateDayOfTheWeek")
async def calc(day: int, month: int, year: int):
    d, m, y = day, month, year
    # same adjustment as the CLI helper
    if m in [1, 2]:
        y -= 1

    if not validate_date(d, m, y):
        raise HTTPException(status_code=400, detail="Invalid date. Please provide a valid DD/MM/YYYY.")

    day_of_week = calculate_day_of_week(d, m, y)
    return {"day_of_week": day_of_week}


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
        

