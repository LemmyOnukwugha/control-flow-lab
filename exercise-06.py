inp_month = input ("Enter the month of the year (Jan - Dec):")
inp_day = int(input ("Enter the day of the month:"))

#if inp_month = "jan" | inp_month = "feb" | inp_month = "jan" & inp_day < 22 | inp_month = "mar" & inp_day < 20
if inp_month in ('Jan', 'Feb'):
    season = 'winter'
elif inp_month in ('Apr', 'May'):
    season = 'spring'
elif inp_month in ('Jul', 'Aug'):
    season = 'summer'
elif inp_month in ('Oct', 'Nov'):
    season = 'fall'
elif inp_month == "Dec":
    if inp_day < 21:
        season = 'fall'
    else:
        season = 'winter'
elif inp_month == "Mar":
    if inp_day < 20:
        season = 'winter'
    else:
        season = 'spring'
elif inp_month == "Jun":
    if inp_day < 21:
        season = 'spring'
    else:
        season = 'summer'
elif inp_month == "Sep":
    if inp_day < 22:
        season = 'summer'
    else:
        season = 'fall'   


print(f"{inp_month} {inp_day} is in {season} ")