# Simple ATM Balance Checking System

correct_pin = 2346
balance = 25000.00

pin = input("Enter your 4-digit ATM PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")
    print("Your current bank balance is ₹", balance)
else:
    print("\nIncorrect PIN!")
    print("Please try again.")