# Is it a Leap Year?

y = int(input("Type any year to see if it's a leap year: "))
rest = y % 4
if rest == 0 and y % 100 != 0 or y % 400 == 0:
    print("Yes, it's a leap year.")
else:
    print("This is not a leap year.")
