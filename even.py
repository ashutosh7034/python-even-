def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

user_number = int(input("Enter a number: "))

if is_even(user_number):
    print(f"{user_number} is even.")
else:
    print(f"{user_number} is odd.")
