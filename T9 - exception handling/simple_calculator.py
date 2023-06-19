# Calculator function - performs operations and write to calculations.txt
def calculate():
    while True:
        try:
            # ask for user input
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            operator = input(
                """Enter one of the following operators
                    '+' (add)
                    '-' (subtract)
                    '*' (multiply)
                    '/' (divide)
                                   : """
            )
            # Determining the operator selected and output calc
            if operator == "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operator == "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operator == "*":
                result = num1 * num2
                print(f"{num1} x {num2} = {result}")
            elif operator == "/":
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid input. Please try again.")
                continue

            # (create and) append equation to calculations.txt
            with open("calculations.txt", "a") as file:
                file.write(f"{num1} {operator} {num2} = {result}\n")

            break

        # Catch errors caused by invalid inputs
        except:
            print("Invalid Input")

# open and read past calcualtions from file
def read_calc():
    while True:
        try:
            file_name = input(
                "Enter the name of the file you would like to read from: "
            )
            file = open(file_name, "r")
            print(file.read())
            file.close()
            break
        except FileNotFoundError:
            print(
                "File not found. Make sure to use the correct name e.g. 'filename.txt'."
            )
            continue


# User selects function they would like to use
while True:
    choice = input(
        """
    Enter '1', '2', or '3' to selct on of the following:
    1: Calculate
    2: Read Calculate file
    3: Exit\n
    """
    )
    if choice == "1":
        calculate()
    elif choice == "2":
        read_calc()
    elif choice == "3":
        print("\nGoodbye")
        break
    else:
        print("Invalid input. Try again.")
        continue
