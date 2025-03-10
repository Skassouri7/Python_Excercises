print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
    if age >= 16:
        print("You can ride the rollercoaster")
    else:
        print("Sorry you have to grow older before you can ride.")
else:
    print("Sorry you have to grow taller before you can ride.")
