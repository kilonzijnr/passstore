class User:
        """
        A Class that generates new user credentials
        """


        User_lst = []


        def __init__(self, first_name, last_name,user_name, password, email):
            """
                __init__ method that helps us define properties for our objects.

                Args:
                    first_name: New User first name.
                    last_name : New User last name.
                    user_name:Username for new user.
                    password: New user password.
                    email : New user email address.
                    """

            self.first_name = first_name
            self.last_name = last_name
            self.user_name = user_name
            self.password = password
            self.email = email


        def save_User(self):
            """
            saves users credatials to user_lst
            """
            User.User_lst.append(self)


        def delete_User(self):
                """
                remove_user removes User objects from user_lst
                """
                User.user_lst.remove(self)

        @classmethod

        def User_login(cls, user_name, password):
                """
                user_login checks whether username and password are correct
                """
                for User in cls.User_lst:
                    if User.user_name == user_name and User.password == password:
                        return True
