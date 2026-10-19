# ===== DATA: menus and prices live here, in one place =====
# Each key is the number the user types; each value is what they are choosing.
MODELS ={
    "1": "MacBook Air 2019",
    "2": "MacBook Pro 2020",
    "3": "MacBook Pro 2021"
}
SERVICES = {
    "1": ("Screen Repair", 200),
    "2": ("Battery Replacement", 500),
    "3": ("Water Damage", 800),
    "4": ("Keyboard Replacement", 300)
}

# ===== THE GREETING SECTION =====

# Shows a welcome message when the chatbot starts.
def greet():
    print("=" * 45)
    print("Welcome to the MacBook Repair Quote Chatbot!")
    print("I'll collect your details, then help you build a quote.")
    print("=" * 45)
    print()

#==========THE USER INFORMATION SECTION==============

#this function collects user information 
def get_user_info():  # a function: a named block of code you can run whenever you call it
    name = input("Enter your first name: ")  # variables: each holds one answer
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    return name, surname, phone_number, email #Returns the collected information as tuple.

#=======THE MACBOOK SELECTION SECTION==========

# This funtion prompts the user to choose between  Macbooks.
def select_macbook_model():
    # Joins the dictionary keys into text like "1, 2, 3", so the prompts
    # update automatically when an item is added to the menu.
    options = ", ".join(MODELS)
    # Start an infinite loop so the user MUST choose a valid option
    while True:
        print("\nSelect your MacBook: ")
        for number, model in MODELS.items():
            print(f"{number}. {model}")
        choice = input(f"Enter your choice from {options}: ")

        # If valid, return the choice and exit the function
        if choice in MODELS:
            return MODELS[choice]
        # If the input is not valid, tell the user and repeat the loop
        else:
            print(f"\nInvalid choice. Please enter from {options}.")

# ===== THE SERVICES SECTION ================
# This function asks the user to choose a service and returns its name and price.
def select_service():
    options = ", ".join(SERVICES)
    # Loop until the user picks a valid number
    while True:
        print("\n--- Available Services ---")
        for number, (name, price) in SERVICES.items():
            print(f"{number}. {name}: R{price}")

        choice = input(f"\nEnter from {options}: ")

        if choice in SERVICES:
            service_name, selected_price = SERVICES[choice]
            return {
                "service_name": service_name,
                "price": selected_price
            }
        else:
            print(f"\nInvalid choice. Please enter from {options}.")

# Asks whether the customer wants another service. Returns True or False.
def ask_add_another():
    while True:
        answer = input("\nAdd another service? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please enter y or n.")

# ===== THE MAIN PROGRAM SECTION =====

# main() holds the order of events: collect details, choose a MacBook,
# choose a service, then print the receipt.
# The variables created inside it only exist while main() is running.      
def main():
    greet()
    user_info = get_user_info()
    print(f"\nThanks, {user_info[0]}! Let's find your MacBook.")

    selected_choice = select_macbook_model()
    print("\nselected MacBook:", selected_choice)
    # Create an empty list. This is the "cart" that will hold the chosen services.
    order_items = []   # the "cart": starts empty
    while True:
        # Ask the customer to pick a service. This returns a dictionary
        # such as {"service_name": "Screen Repair", "price": 200}.
        item = select_service()
        # Is this exact service already in the cart?
        if item in order_items:
            # Yes, so tell the customer and don't add it a second time.
            print(f"\n{item['service_name']} is already in your quote.")
        else:
            # No, so put it in the cart.
            order_items.append(item)
            # Confirm what was added
            print(f"\nAdded: {item['service_name']}")
        # Ask "Add another service? (y/n)". It returns True for y and False for n.
        # "not" flips that, so this reads: if the answer is NOT yes...
        if not ask_add_another():
              # ...stop the loop and move on to the receipt.
            break
    # Start the running total at zero.
    total = 0
    # Go through the cart one service at a time.
    for item in order_items:
        # Add this service's price to the total (200, then 200 + 500, and so on).

        total = total + item["price"]

    print("\n--- Final Receipt ---")
    print(f"Customer: {user_info[0]} {user_info[1]}")
    print(f"MacBook:  {selected_choice}")
    print("Services:")
    for item in order_items:
        print(f"  - {item['service_name']}: R{item['price']}")
    print(f"Total Cost: R{total}")
    
# Guard: Python labels this file "__main__" when it is run directly
# (python3 chatbot.py) and "chatbot" when another file imports it.
# main() only starts the chatbot in the first case, so other code
# (tests, a web app, CI) can import the functions safely.

if __name__ == "__main__":
    main()