from calendar import day_name, weekday
month, day, year = map(int, input().split())
print(day_name[weekday(year, month, day)].upper())
