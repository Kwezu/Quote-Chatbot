# ===== DATA: menus and prices live here, in one place =====
# Each key is the number the user types; each value is what they are choosing.
MODELS = {
    "1": "MacBook Air 13-inch (2018-2019, Intel)",
    "2": "MacBook Air 13-inch (2020, Intel)",
    "3": "MacBook Air 13-inch (2020, M1)",
    "4": "MacBook Air 13-inch (2022, M2)",
    "5": "MacBook Pro 13-inch (2019-2020, Intel)",
    "6": "MacBook Pro 13-inch (2020, M1)",
    "7": "MacBook Pro 14-inch (2021, M1 Pro/Max)",
    "8": "MacBook Pro 16-inch (2019, Intel)",
    "9": "MacBook Pro 16-inch (2021, M1 Pro/Max)",
    "10": "MacBook Pro 14-inch (2023, M2 Pro/Max)",
    "11": "MacBook Air 15-inch (2023, M2)"
}
SERVICES = {
    "1": ("Diagnostic Check", 350),
    "2": ("Screen Replacement", 4500),
    "3": ("Battery Replacement", 1800),
    "4": ("Keyboard Replacement", 3200),
    "5": ("Trackpad Replacement", 1900),
    "6": ("Charging Port Repair", 1200),
    "7": ("Fan Replacement / Cleaning", 950),
    "8": ("Liquid Damage Cleaning", 1500),
    "9": ("Logic Board Repair", 5500)
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
def get_user_info():
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    return {
        "name": name,
        "surname": surname,
        "phone_number": phone_number,
        "email": email
    }

 #=======THE MACBOOK SELECTION SECTION==========

# This function prompts the user to choose between MacBooks.
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


 #===== THE SERVICES SECTION ================

 

# Asks whether the customer wants another service. Returns True or False.
def ask_add_another():
    while True:
        answer = input("\nAdd another service? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please enter y or n.")

# ===== THE REUSABLE MENU SECTION =====

# Shows a numbered menu, keeps asking until the user picks a valid number,
# then returns the chosen option.
#   title    - the heading to print above the menu
#   options  - a dictionary like MODELS or SERVICES
#   describe - a small function that turns ONE option into the text to display
def choose_from_menu(title, options, describe):
    keys = ", ".join(options)
    while True:
        print(f"\n--- {title} ---")
        for number, value in options.items():
            print(f"{number}. {describe(value)}")

        choice = input(f"\nEnter your choice from {keys}: ")

        if choice in options:
            return options[choice]
        print(f"\nInvalid choice. Please enter from {keys}.")

# Turns one SERVICES entry, like ("Screen Repair", 200), into display text.
def describe_service(service):
    name, price = service
    return f"{name}: R{price}"
# ===== THE MAIN PROGRAM SECTION =====

# main() holds the order of events: collect details, choose a MacBook,
# choose a service, then print the receipt.
# The variables created inside it only exist while main() is running.      
def main():
    greet()
    user_info = get_user_info()
    print(f"\nThanks, {user_info['name']}! Let's find your MacBook.")

    selected_choice = choose_from_menu("Select your MacBook", MODELS, lambda model: model)
    print("\nselected MacBook:", selected_choice)
    # Create an empty list. This is the "cart" that will hold the chosen services.
    order_items = []   # the "cart": starts empty
    while True:
        # Ask the customer to pick a service. This returns a dictionary
        # such as {"service_name": "Screen Repair", "price": 200}.
        service_name, price = choose_from_menu("Available Services", SERVICES, describe_service)
        item = {"service_name": service_name, "price": price}
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
    print(f"Customer: {user_info['name']} {user_info['surname']}")
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