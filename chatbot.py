#this function collects user information 
def get_user_info():
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    email = input("Entwe your email address: ")
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
            print("Invalid choice. Please enter 1 or 2.")
# this function generates a quotaion based on the selected Macbook model and service chosen by the user.

selected_choice = select_macbook_model()
print("\nuser name",user_info)
print("selected MacBook:",selected_choice)

def generate_quotaion(choice):
    #simple pricing for demonstarion 
    prices ={
        "1": {"screen_repair":300},
        "2": {"battery_change":400}
    }
    print("\n-- Available Services---")
    print("1. Screen Repair")
    print("2.Battery Change")

service_choice = input("select a service (1.Screen_repair or 2.Battery Change):" )

service_map = {
        "1": "screen_repair",
        "2": "battery_change"
}

