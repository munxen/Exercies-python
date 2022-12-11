#9-7. Administrator: Administrator is a special kind of user. Write a class named Admin, 
# inheriting from the User class from Exercise 9-3 (p. 165) or exercise 9-5 (p. 170). Add an attribute 
# privileges for storing a list of lines like "allowed to add messages", "allowed to delete users",
# "it is allowed to ban users", etc. Write the show_privileges() method to output a set of privileges 
# admin. Create an instance of Admin and call your method.

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
    def privileges(self,):
        """Admin's priveleges"""
        self.permission_admin=['ban users','add messages','delete users']
    def show_privilieges(self):
        print("You are permissions: " + {self.permission_admin})
user_1=Admin('Spyder','Man',24,'USA')
user_1.describe_user()
user_1.show_privilieges()
    