MODELS ={
    "1": "MacBook Air 2019",
    "2": "MacBook Pro 2020",
    "3": "MacBook Pro 2021"
}
#this function collects user information 
def get_user_info():  # a function: a named block of code you can run whenever you call it
    name = input("Enter your first name: ")  # variables: each holds one answer
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    return name, surname, phone_number, email #Returns the collected information as tuple.

user_info = get_user_info()
print("\nuser information:",user_info)

# This funtion prompts the user to choose between two Macbooks.
def select_macbook_model():
    # Start an infinite loop so the user MUST choose a valid option
    while True:
        print("\nSelect your MacBook: ")
        for number, model in MODELS.items():
            print(f"{number}. {model}")
        choice = input("Enter 1,2 or 3: ")

        # If valid, return the choice and exit the function
        if choice in MODELS:
            return MODELS[choice]
        # If the input is not valid, tell the user and repeat the loop
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
# this function generates a quotaion based on the selected Macbook model and service chosen by the user.

selected_choice = select_macbook_model()
print("\nuser information:",user_info)
print("\nselected MacBook:",selected_choice)

def select_service():
    # 1. Our "Menu" dictionary 
    services = {
       "1" : ("Screen Repair", 200),
       "2" :("Battery Replacement", 500),
       "3" : ("Water Damage", 800)
      
    }
# loop untilee the user pick a valid number
    while True:
        print("\n--- Available Services ---")
        for number, (name, price) in services.items():
            print(f"{number}. {name}: R{price}")

        choice = input("\nEnter 1, 2 , 3: ")

        if choice in services:
            service_name, selected_price = services[choice]
            return {
                "service_name": service_name,
                "price": selected_price
            }
        else:
            print("\nInvalid choice. Please enter 1, 2 or 3.")
# --- Using the Function ---
order_info = select_service()


print("\n--- Final Receipt ---")
print("select_service: " + order_info["service_name"])
print("Total Cost: R" + str(order_info["price"]))
