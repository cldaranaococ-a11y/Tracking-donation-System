import datetime

accounts = {
    "treasurer": {"username": "treasurer1", "password": "pass123"},
    "leader": {"username": "leader1", "password": "admin123"}
}

donors = []   # list to store donor names
amounts = []  # list to store donation amounts


# --- LOGIN FUNCTION ---
def login(role):
    print(f"\n===== {role.upper()} LOGIN =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == accounts[role]["username"] and password == accounts[role]["password"]:
        print(" Login successful!\n")
        return True
    else:
        print(" Invalid username or password!\n")
        return False


# --- TREASURER MENU ---
def treasurer_menu():
    while True:
        print("\n===== TREASURER MENU =====")
        print("1. Input donor and amount")
        print("2. Track total collected")
        print("3. Go back")
        choice = input("Enter your choice: ")

        if choice == "1":
            donor = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
                donors.append(donor)
                amounts.append(amount)
                print(f" Donation from {donor} of ₱{amount:.2f} recorded successfully!")
            except ValueError:
                print(" Invalid amount! Please enter a number.")
        elif choice == "2":
            total = sum(amounts)
            print(f" Total funds collected so far: ₱{total:.2f}")
        elif choice == "3":
            break
        else:
            print(" Invalid choice, please try again.")


# --- ORGANIZATION LEADER MENU ---
def leader_menu():
    while True:
        print("\n===== ORGANIZATION LEADER MENU =====")
        print("1. View donor list")
        print("2. Monitor total funds raised")
        print("3. Go back")
        choice = input("Enter your choice: ")

        if choice == "1":
            if len(donors) == 0:
                print(" No donors yet.")
            else:
                print("\n--- Donor List ---")
                for i in range(len(donors)):
                    print(f"{i+1}. {donors[i]} - ₱{amounts[i]:.2f}")
        elif choice == "2":
            total = sum(amounts)
            print(f" Total funds raised: ₱{total:.2f}")
        elif choice == "3":
            break
        else:
            print(" Invalid choice, please try again.")


# --- MAIN PROGRAM ---
def main():
    print("=======================================")
    print("      DONATION TRACKING SYSTEM")
    print("=======================================")
    print("Date:", datetime.date.today())

    while True:
        print("\nSelect Role:")
        print("1. Treasurer")
        print("2. Organization Leader")
        print("3. Exit")
        role_choice = input("Enter your role: ")

        if role_choice == "1":
            if login("treasurer"):
                treasurer_menu()
        elif role_choice == "2":
            if login("leader"):
                leader_menu()
        elif role_choice == "3":
            print(" Thank you for using the system. Goodbye!")
            break
        else:
            print(" Invalid input, please try again.")

# Run the program
main()