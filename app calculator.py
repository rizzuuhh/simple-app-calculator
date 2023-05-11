import pyfiglet

# Print the title of program
title = pyfiglet.figlet_format("SIMPLE APP CALCULATOR", font = "bulbhead" )
print(title)

repeat = True

while repeat:
    # Ask the user for there desired operation
    print("\033[36mChoose an operation:")
    add = pyfiglet.figlet_format("1 Addition", font = "bubble" )
    print("\033[35m" + add)

    sub = pyfiglet.figlet_format("2 Subtraction", font = "bubble" )
    print("\033[35m" + sub)

    mul = pyfiglet.figlet_format("3 Multiplication", font = "bubble" )
    print("\033[35m" + mul)

    div = pyfiglet.figlet_format("4 Division", font = "bubble" )
    print("\033[35m" + div)

    try:
        user_choice = int(input("\033[31mEnter your choosen operation (1-4): "))
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
    else:
        try:
            result = first_num / second_num


            print(f"The result is: {result} ")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue

    # Ask if the user wants to try again
    try_again = input("\033[33mDo you want to try again? (yes/no): ")
    if try_again.lower() != "yes":
        repeat = False

# Print the output
ty = pyfiglet.figlet_format("THANK YOU", font = "bulbhead" )
print("\033[29m" + ty)