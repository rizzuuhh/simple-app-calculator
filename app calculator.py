# Print the title of program
title = "SIMPLE APP CALCULATOR"
print(title)

repeat = True

while repeat:
    # Ask the user for there desired operation
    print("Choose an operation:")
    add = ("1 Addition")
    print(add)

    sub = ("2 Subtraction")
    print(sub)

    mul = ("3 Multiplication")
    print(mul)

    div = ("4 Division")
    print(div)

    try:
        user_choice = int(input("Enter your choosen operation (1-4): "))
        if user_choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please enter a valid choice.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Ask user to enter the numbers to be calculated
    try:
        first_num = float(input("Enter the 1st number: "))
        second_num = float(input("Enter the 2nd number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Perform the selected operation and print the result of calculation
    if user_choice == 1:
        result =  first_num +  second_num
        print(f"The result is: {result}")
    elif user_choice == 2:
        result = first_num - second_num
        print(f"The result is: {result}")
    elif user_choice == 3:
        result = first_num * second_num
        print(f"The result is: {result}")


# Ask if the user wants to try again
# Print the output
