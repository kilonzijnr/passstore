from _typeshed import Self


class User:

    """
 A Class that generates new user credentials
    """


User_lst = []


def __init__(self, first_name, last_name, password, email):
    """
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New User first name.
            last_name : New User last name.
            password: New user password.
            email : New user email address.
            """

    Self.first_name = first_name
    Self.last_name = last_name
    Self.password = password
    Self.email = email

def save_user(self):
    """
    saves users credatials to user_lst
    """
    User.user_lst.append(self)

    def remove_user(self):

        """
        remove_user removes User objects from user_lst
        """
        User.user_lst.remove(self)

    @classmethod

    def user_login(cls, user_name, password):

        """
        user_login checks whether username and password are correct
        """
        
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                return True