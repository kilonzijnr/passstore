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
