# Function that will print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Horchata")
    print("5. Quit")


# Function that retrieves the price and item name based on user selection
def get_item_info(choice):
    if choice == 1:
        return "Taco", 2.99
    elif choice == 2:
        return "Burrito", 4.99
    elif choice == 3:
        return "Nachos", 6.99
    elif choice == 4:
        return ("Horchata"), 3.50
    else:
        return "", 0.0


def main():
    # Initialize variables and list
    ordered_items = []
    total_price = 0.0

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    # Loop until the user chooses the quit option
    while True:
        print_menu()

        # Get integer input from the user
        try:
            choice = int(input("User entered: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            break
        elif choice >= 1 and choice <= 4:
            item_name, item_price = get_item_info(choice)
            print(f"You selected a {item_name}")

            # Update total amount due and store item in the list
            total_price += item_price
            ordered_items.append(item_name)
        else:
            print("Invalid selection. Please choose a number from the menu.")

    # Format and print the final order summary
    if len(ordered_items) > 0:
        # Create a string representation of the list (i.e. food ordered)
        if len(ordered_items) == 1:
            item_summary = ordered_items[0]
        elif len(ordered_items) == 2:
            item_summary = f"{ordered_items[0]} and a {ordered_items[1]}"
        else:
            item_summary = ", ".join(ordered_items[:-1]) + f", and a {ordered_items[-1]}"

        print(f"\nYou ordered {item_summary}. Your total is ${total_price:.2f}")
    else:
        print("\nYou didn't order anything")


# Execute the program
if __name__ == "__main__":
    main()