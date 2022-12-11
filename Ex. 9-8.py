#Privileges: Write the Privileges class. The class must contain only one privileges attribute with a list of strings 
# from exercise 9-7. Move the show_privileges() method to this class. Create an instance of Privileges as 
# attribute of the Admin class. Create a new Admin instance and use your method to list privileges.

class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name =first_name+last_name
        self.age = age
        self.country = country
    def describe_user(self):
        print("\nUser info:" + "\n" + self.first_name.title())
        print("" + self.last_name.title())
        print("" + str(self.age))
        print("" + self.country.title())
    def greet_user(self):
        print("\nHello " + self.full_name)
class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        """The inheritance from the User class"""
        super().__init__(first_name, last_name, age, country)
    def privileges(self):
        """Admin's Privileges"""
        self.permission_admin=['ban users','add messages','delete users']
    def show_privilieges(self):
        print("You are permissions: " + {self.permission_admin} )
class Privileges():
    """Privileged class"""
    def __init__(self,):
        """Creates a list of privileges"""
        self.privileges =['add users','delete users','delete messages']
    def show_privileges(self):
        """Displays a list of privileges"""
        print("You a permissions are: " + str(self.privileges))
class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        """The inheritance from the User class"""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()
user1=Admin('Spider','Man',23,'usa')
user1.describe_user()
user1.privileges.show_privileges()
