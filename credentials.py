from userlogin import User
import random, string

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