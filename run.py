from userlogin import User
from credentials import credentials

def new_user(first_name, last_name, user_name, email, password):
    """
    Function using the User class to build a new_user
    Args:
    first_name: user's first name
    last_name: user's last name
    user_name: username used to login
    email: email attached to login
    password: user's new password for login access
    Returns: new_user
    """
    new_user = User(first_name, last_name, user_name, email, password)
    return new_user

def save_user(User):
    """
    Function saves the new user credentials for login
    """
    User.save_user(User)

def validate_user(user_name, password):
    """
    Function to validate if user exists in user_lst
    """
    check_user = credentials.validate_user(user_name, password)
    return check_user

def new_credentials(web_name, user_name, password):
    """
    Function for creating new credentials
    """
    new_credentials = credentials(web_name, user_name, password)
    return new_credentials

def save_credentials(credentials):
    """
    Function for saving new credentials input
    """
    credentials.save_credentials(credentials)

def list_credentials(User):
    """
    Function for listing credentials per user
    """
    return credentials.list_credentials(User)

def password_creator():
    """
    Function calling the password_creator from the credentials file
    """
    password = credentials.password_creator()
    return password

def run():
    print(" ")
    print("*")
    print("HELLO, WELCOME TO Password Store")
    print("*")
    while True:
        print(" ")
        print("=")
        print(" ")
        print(
            "Kindly use the options below to navigate through the app: \n 1 ==> Sign Up \n 2 ==> Log In \n 3 ==> Exit"
        )
choice = str(input("Enter option: "))
        if choice == "1":
            print("=")
            print(" ")
            print("Creating Account")
            print(" ")
            first_name = input("Input your first name ==> ").strip()
            last_name = input("Enter your second name ==> ").strip()
            user_name = input("Input a username ==> ").strip()
            email = input("Enter your email ==> ").strip()
            password = input("Enter your a new password ==> ").strip()
            save_user(new_user(first_name, last_name, user_name, email, password))
            print(" ")
            print(
                f"Account created succesfully!: \n First Name: {first_name} \n Surname: {last_name} \n Username: {user_name} \n Email: {email} \n Password: {password}"
            )
            print(" ")
            print(
                "Do not forget or disclose your password! Also note that your password is only accessible to you!"
            )
        elif choice == "2":
            