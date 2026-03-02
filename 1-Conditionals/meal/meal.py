def main():
    meal_time = input('What meal time is it? ')
    hours, minutes = meal_time.split(':')

    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60

    time = hours + minutes
    print(convert(time))

def convert(time):
    if time >= 7.0 <= 8.0:
        return('Breakfast time')
    elif time >= 12.0 <= 13.0:
        return('Lunch time')
    elif time >= 18.0 <= 19.0:
        return('Dinner time')

main()
