from userlogin import User
from credentials import Credentials

def new_User(first_name, last_name, user_name, email, password):
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
    new_user=User(first_name, last_name, user_name, email, password)
    return new_user

def save_User(user):
    """
    Function saves the new user credentials for login
    """
    User.save_User(user)

def validate_User(user_name, password):
    """
    Function to validate if user exists in user_lst
    """
    validate_User = Credentials.validate_User(user_name, password)
    return validate_User

def new_credentials(web_name, user_name, password):
    """
    Function for creating new credentials
    """
    new_credentials = Credentials(web_name, user_name, password)
    return new_credentials

def save_credentials(credentials):
    """
    Function for saving new credentials input
    """
    Credentials.save_credentials(credentials)

def list_credentials(User):
    """
    Function for listing credentials per user
    """
    return Credentials.list_credentials(User)

def password_creator():
    """
    Function calling the password_creator from the credentials file
    """
    password = Credentials.password_creator()
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
                    print("Create an Account")
                    print(" ")
                    first_name = input("Input your first name >>> ").strip()
                    last_name = input("Enter your second name >>> ").strip()
                    user_name = input("Input a username >>> ").strip()
                    email = input("Enter your email >>> ").strip()
                    password = input("Enter your new password >>> ").strip()
                    save_User(new_User(first_name, last_name, user_name, email, password))
                    print(" ")
                    print(
                        f"Account created succesfully!: \n First Name: {first_name} \n Surname: {last_name} \n Username: {user_name} \n Email: {email} \n Password: {password}"
                    )
                    print(" ")
                    print(
                        " Kindly do not forget your login credentials!"
                    )
                    print(" ")
                    print(
                        "Now you can Login into your acount"
                    )
        elif choice == "2":
                    print(" ")
                    print("Log in to your Account")
                    print(" ")
                    username = input("Input your username >>> ").strip()
                    password = str(input("Input your password >>> "))
                    username = validate_User(user_name, password)
                    if username == user_name:
                        print(" ")
                        print(
                            f"Hey {user_name} !.\nKindly select an option to continue: "
                        )
                        while True:
                            print(" ")
                            print(
                                "Select an option: \n 1 ==> Save your new credentials \n 2 ==> Show saved credentials \n 3 ==> Return to main menu"
                            )
                            option = input("Input your option: ").strip()
                            print(" ")
                            if option == "1":
                                print(" ")
                                print("Input new credentials:")
                                web_name = input(r"Enter the application's name ==> ").strip()
                                user_name = input(r"Enter your application's account name ==> ")
                                while True:
                                    print(" ")
                                    print(
                                        "Kindly select an option \n 1 ==> Auto-generate a password \n 2 ==> Create your own password \n 3 ==> Back"
                                    )
                                    choice = input("Select an option: ")
                                    print("=")
                                    if choice == "2":
                                        print(" ")
                                        password = input(
                                            "Input your application's password: "
                                        ).strip()
                                        break
                                    elif choice == "1":
                                        password = password_creator()
                                        break
                                    elif choice == "3":
                                        break
                                    save_credentials(
                                    new_credentials(web_name, user_name, password)
                                )
                                print(" ")
                                print(
                                    f"New credentials saved: \n Application/Website: {web_name} \n User Name: {user_name} \n User's Password: {password} "
                                )
                                print(" ")
                            elif option == "2":
                                print(" ")
                                if list_credentials(user_name):
                                    print("Credentials:")
                                    print(" ")
                                    for credentials in list_credentials(user_name):
                                        print(
                                            f"Application/Website: {credentials.web_name} \n User Name: {credentials.user_name} \n Password: {credentials.password}"
                                        )
                                    print(" ")
                                else:
                                    print(
                                    "There are no credentials saved under you account. Kindly select option 1 to save current credentials"
                                    )
                                    print(
                                    "User not found!.Select option 1 to Create a new Account"
                                )
        elif choice == "3":
                    print(" ")
                    print("Thankyou for using the app!")
                    break


if __name__ == "__main__":
     run()