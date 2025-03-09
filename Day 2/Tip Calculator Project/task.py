print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip  = (1 + tip/100)
individualBill = float((bill / 5) * tip )
print(tip)
print(format(individualBill, '.2f'))

