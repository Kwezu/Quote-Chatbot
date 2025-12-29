#this function collects user information 
def get_user_info():
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    return name, surname, phone_number, email #Returns the collected information as tuple.

user_info = get_user_info()
print("\nuser name",user_info)

# This funtion prompts the user to choose between two Macbooks.
def select_macbook_model():
    models = {
        "1": "MacBook Air 2019",
        "2": "MacBook Air 2020"
    }  
    # Start an infinite loop so the user MUST  choose a valid option
    while True:
          print("\nSelect your MacBook: ")
          print("1. MacBook Air 2019: ")
          print("2. MacBook Pro 2020: ")
          choice = input ("Enter 1 or 2: ")

        #Check if the user enter theier choice 
          if choice in models:
            
            return models[choice]
            #if valid return the choice and exit the funtion 
        #If the input is not valid, tell the user and repeat the loop
          else:
            print("\nInvalid choice. Please enter 1 or 2.")
# this function generates a quotaion based on the selected Macbook model and service chosen by the user.

selected_choice = select_macbook_model()
print("\nuser name",user_info)
print("\nselected MacBook:",selected_choice)

def select_service():
    # 1. Our "Menu" dictionary
    services = {
        "Screen Repair": 200,
        "Battery Replacement": 500,
        "Water Damage": 800
    }

    print("--- Available Services ---")
    # Displaying the options to the user
    for item, price in services.items():
        print(f"- {item}: ${price}")

    # 2. Capture the user's choice
    choice = input("\nWhich service do you need? ")

    # 3. Logic to "fetch" the price from our dictionary
    if choice in services:
        selected_price = services[choice]
        
        # 4. Pack the information to "Return" it
        return {
            "service_name": choice,
            "price": selected_price
        }
    else:
        print("Invalid service selected.")
        return None

# --- Using the Function ---
order_info = select_service()

if order_info:
    print("\n--- Final Receipt ---")
    print("Service: " + order_info["service_name"])
    print("Total Cost: R" + str(order_info["price"]))
