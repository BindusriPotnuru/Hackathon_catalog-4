import getpass

def level_one_authentication():
    # Simple textual password authentication
    password = getpass.getpass("Enter Level 1 Password: ")
    if password == "passport":  # Replace with your secure password
        return True
    return False

def level_two_authentication():
    # Example of a graphical password represented by a simple pattern
    # For simplicity, let's assume it is a 3x3 grid and the correct pattern is [1, 5, 9]
    print("Enter the pattern by selecting numbers in a 3x3 grid (1-9):")
    pattern = input("Pattern: ")
    if pattern == "143":  # Replace with the actual pattern
        return True
    return False

def level_three_authentication():
    # Simple biometric voice authentication simulation (here using a passphrase)
    # This is highly simplified and not a real biometric system
    phrase = getpass.getpass("Speak the passphrase: ")
    if phrase.lower() == "paypal":  # Replace with actual passphrase
        return True
    return False

def three_level_password_system():
    print("Three-Level Password System")
    
    if not level_one_authentication():
        print("Level 1 Authentication Failed")
        return

    print("Level 1 Authentication Successful")

    if not level_two_authentication():
        print("Level 2 Authentication Failed")
        return

    print("Level 2 Authentication Successful")

    if not level_three_authentication():
        print("Level 3 Authentication Failed")
        return

    print("Level 3 Authentication Successful")
    print("Access Granted!")

# Run the system
three_level_password_system()
