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

