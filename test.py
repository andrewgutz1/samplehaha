while True:
    try:
        age = int(input("Enter your age: "))
    
        if age >= 18:
             print("You are allowed to enter!")
             break# Exit the loop when age is 18
        else:
            print("You are not allowed to Enter")
            print("Please Try AgaiN")

    except ValueError:
        print("Invalid input! Please enter a number.")
