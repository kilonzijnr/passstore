from userlogin import User
import random
import string


class credentials:
    """
    credentials class to create new user credentials
    """

    credentials_list = []


def __init__(self, web_name, user_name, password):
    """
    __init__ to define properties of new user Credentials
    Args:
        web_name: site to which the credentials belong to
        user_name: username for website's account user
        password: password for specific account user
    """
    self.web_name = web_name
    self.user_name = user_name
    self.password = password


def save_credentials(self):
    """
    save_credentials saves new instances of credentials in the list
    """
    credentials.credentials_list.append(self)


def delete_credentials(self):
    """
    delete_credentials removes existing instances of credentials
    """
    credentials.credentials_list.remove(self)


@classmethod
def find_by_web_name(cls, web_name):
    """
    The function takes the web_name and returns credentials that match to it
    """


    for credential in cls.credentials_list:
        if credential.web_name ==web_name:
            return credential


@classmethod
def list_credentials(cls, user_name):
    """
    This method returns the credentials array
    """
    user_credentials_list = []
    for credential in cls.credentials_list:
        if credential.user_name == user_name:
            user_credentials_list.append(credential)
    return user_credentials_list


@classmethod
def validate_user(cls, user_name, password):
    """
    function to validate if user exists in user_lst
    """
    validated_user = ""
    for user in User.user_list:
        if user.user_name == user_name and user.password == password:
            validated_user = user.user_name
        return validated_user


def password_creator(
        size=8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits
):
    """
    Function to auto-generate passwords for users
    """
    password = "".join(random.choice(char) for _ in range(size))
    return password
