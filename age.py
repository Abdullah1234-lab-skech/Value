def age_counter():
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Error: Age must be a positive number.")
        else:
            print(f"Your age is {age}.")
            if age % 2 == 0:
                print("It's an even number.")
            else:
                print("It's an odd number.")
    except ValueError:
        print("Error: Please enter a valid number.")

age_counter()
