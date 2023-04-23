# Price varys accordinly to travel distance. It costs $0.50 per mile up to 200 miles, and $0.45 for longer trips.

d = float(input("Type the travel distance: "))
if d <= 200:
    print("Your ticket price is ${}".format(d*0.5))
else:
    print("Your ticket price is ${}".format(d*0.45))
