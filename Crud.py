# Simple CRUD Program in Python

# Our data store (list of dictionaries)
users = []

def create_user():
    """Add a new user"""
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    users.append({"name": name, "age": age, "email": email})
    print(f"\n✅ User '{name}' added successfully!\n")

def read_users():
    """Display all users"""
    if not users:
        print("\n📭 No users found.\n")
    else:
        print("\n📋 List of Users:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
        print()

def update_user():
    """Update user information"""
    read_users()
    if users:
        try:
            index = int(input("Enter the number of the user to update: ")) - 1
            if 0 <= index < len(users):
                user = users[index]
                print("\nLeave blank if you don't want to change a field.")
                new_name = input(f"New name ({user['name']}): ") or user['name']
                new_age = input(f"New age ({user['age']}): ") or user['age']
                new_email = input(f"New email ({user['email']}): ") or user['email']

                users[index] = {"name": new_name, "age": new_age, "email": new_email}
                print("\n✅ User updated successfully!\n")
            else:
                print("\n⚠️ Invalid user number.\n")
        except ValueError:
            print("\n⚠️ Please enter a valid number.\n")

def delete_user():
    """Delete a user"""
    read_users()
    if users:
        try:
            index = int(input("Enter the number of the user to delete: ")) - 1
            if 0 <= index < len(users):
                deleted = users.pop(index)
                print(f"\n🗑️ User '{deleted['name']}' deleted successfully!\n")
            else:
                print("\n⚠️ Invalid user number.\n")
        except ValueError:
            print("\n⚠️ Please enter a valid number.\n")

def menu():
    """Main menu"""
    while True:
        print("===== SIMPLE CRUD PROGRAM =====")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("\n👋 Exiting program. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please select 1–5.\n")

# Run the menu
if __name__ == "__main__":
    menu()
