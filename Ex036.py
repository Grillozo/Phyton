# House Loan

from time import sleep
print("-="*30)
print("Welcome to the loan program. Please fill this brief form:")
print("-="*30)
loan = float(input("Enter the total ammount needed: "))
salary = float(input("Enter your monthly income: "))
months = float(input("Loan term (months): "))
payment = loan / months
print("\033[34mYour request is being processed, please wait...\033[m")
sleep(2)
if payment <= salary * 0.3:
    print("\033[32mCongratulations! Your loan is approved and your monthly debt will be ${:.2F}".format(payment))
else:
    print("\033[31mSorry! Your loan was not approved =/")
