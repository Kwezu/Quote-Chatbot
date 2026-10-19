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

    order_info = select_service()

    print("\n==== Final Receipt ====")
    print("\nuser information:", user_info[0], user_info[1])
    print("select_service: " + order_info["service_name"])
    print("Total Cost: R" + str(order_info["price"]))

# Guard: Python labels this file "__main__" when it is run directly
# (python3 chatbot.py) and "chatbot" when another file imports it.
# main() only starts the chatbot in the first case, so other code
# (tests, a web app, CI) can import the functions safely.

if __name__ == "__main__":
    main()