# Read a salary and calc the raise ( if salary > 1250 raise 10% else raise 15%)

s = float(input("Enter your monthly salary: "))
if s > 1250:
    print("You'll have 10% raise, and your new salary will be ${}".format(s+s*0.1))
else:
    print("You'll have 15% raise, and your new salary will be ${}".format(s+s*0.15))
