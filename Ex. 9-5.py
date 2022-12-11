#Login attempts: Add the login_attempts attribute to the User class from Exercise 9-3 (p. 165). Write a method
# increment_login_attempts(), incrementing the value of login_attempts by 1. Write another method named
# reset_login_attempts(), resetting the value of login_attempts.Create an instance of the User class and call
# increment_login_attempts() multiple times. Print the value of login_attempts to make sure that
# the value was changed correctly, and then call reset_login_attempts(). Output login_attempts again
# and make sure that the value is reset to zero.

class User():
    def __init__(self, first_name, last_name, age, country):
        """Create defolt profile (F_name\S_name\T_name, age, country)""" 
        self.first_name = first_name
        self.last_name = last_name
        self.full_name =first_name+last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
    def increment_login_attempts(self):
        """Changes the number of login attempts"""
        self.login_attempts+=1
        print("Login attepts: " + str(self.login_attempts))
    def reset_login_attempts(self):
        """Resets the number of login attempts"""
        self.login_attempts=0
    def read_login_attempts(self):
        """Show, how many was a login attempts """
        print("Login attempts are " + str(self.login_attempts))
    def describe_user(self):
        """We display the profile in one column"""
        print("\nUser info:" + "\n" + self.first_name.title())
        print("" + self.last_name.title())
        print("" + str(self.age))
        print("" + self.country.title())
    def greet_user(self):
        """We welcome individuals"""
        print("\nHello " + self.full_name)
user1=User("lionel","messi",37,"Brazil")
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()
