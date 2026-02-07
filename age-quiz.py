# Request user's age and store as integer
age = int(input("Please enter your age: "))

# Oldest input can be 100
if age > 100:
    print("Sorry, you're dead.")

# Print statements with the following parameters:
if age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")
