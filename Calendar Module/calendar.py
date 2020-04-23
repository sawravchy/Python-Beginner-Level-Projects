import calendar

# print(calendar.weekheader(4))
# print(calendar.firstweekday())
print()
# print(calendar.month(2019,12,4)) # (year,month,weekday name character)
year = int(input("Enter The Year :"))

print(calendar.calendar(year, 3))
is_leap = calendar.isleap(year)
if is_leap:
    print("This year is leap year")
else:
    print(f"Note: {year} is not Leap Year")
    print()
leap_days = calendar.leapdays(2000, year)
print(f"Fun Fact: From 2000 to {year} there are {leap_days} Leap Days :) ")
print()
