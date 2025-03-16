def parse_input(user_input):
    # Parse the user's input into a command and arguments
    cmd, *args = user_input.split()  # Split the input into command and arguments
    cmd = cmd.strip().lower()  # Convert the command to lowercase for consistency
    return cmd, *args  # Return the command and arguments

def add_contact(args, contacts):
    # Add a new contact
    if len(args) != 2:
        return "Invalid command. Please use: add [username] [phone]."
    name, phone = args  # Extract the name and phone number
    contacts[name] = phone  # Add the contact to the dictionary
    return "Contact added."

def change_contact(args, contacts):
    # Change the phone number for an existing contact
    if len(args) != 2:
        return "Invalid command. Please use: change [username] [new phone]."
    name, phone = args  # Extract the name and new phone number
    if name not in contacts:
        return f"Error: Contact '{name}' not found."  # Check if the contact exists
    contacts[name] = phone  # Update the phone number
    return "Contact updated."

def show_phone(args, contacts):
    # Show the phone number for a specific contact
    if len(args) != 1:
        return "Invalid command. Please use: phone [username]."
    name = args[0]  # Extract the name
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"  # Show the phone number
    return f"Error: Contact '{name}' not found."  # Contact not found

def show_all(contacts):
    # Show all contacts
    if not contacts:
        return "No contacts found."  # If no contacts are saved
    result = "All contacts:\n"  # Initialize the result string
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"  # Add each contact to the result
    return result.strip()  # Remove the trailing newline and return the result

def main():
    contacts = {}  # Store contacts in a dictionary
    print("Welcome to the assistant bot!")  # Welcome message
    
    while True:
        user_input = input("Enter a command: ").strip()  # Get user input and strip any leading/trailing whitespace
        command, *args = parse_input(user_input)  # Parse the command and arguments

        if command in ["close", "exit"]:
            print("Good bye!")  # Exit message when closing
            break
        elif command == "hello":
            print("How can I help you?")  # Respond with a help message
        elif command == "add":
            print(add_contact(args, contacts))  # Add a new contact
        elif command == "change":
            print(change_contact(args, contacts))  # Change an existing contact's phone number
        elif command == "phone":
            print(show_phone(args, contacts))  # Show a contact's phone number
        elif command == "all":
            print(show_all(contacts))  # Show all contacts
        else:
            print("Invalid command.")  # If the command is not recognized

if __name__ == "__main__":
    main()  # Run the main function

