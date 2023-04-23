# Triangle inequality theorem

s1 = float(input("Triangle first side length: "))
s2 = float(input("Triangle second side length: "))
s3 = float(input("Triangle third side length: "))

a1 = s1+s2>s3
a2 = s1+s3>s2
a3 = s2+s3>s1

if ((a1 == True) and (a2 == True) and (a3 == True)):
    print("Yes, the 3 sides can form a triangle.")
else:
    print("No, the 3 sides can't make a triangle.")
