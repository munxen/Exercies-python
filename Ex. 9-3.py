#Users: Create a class named User. Create two attributes first_name and last_
# name, and then a few more attributes that are usually stored in the user profile.
#Write the method descripe_user(), which outputs a summary with information about the user.
#Create another greet_user() method to output a personal greeting for the user.Create 
# multiple instances representing different users. Call both methods for each user.

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
user1=User("barak","obama",55,"nigeriya")
user2=User("marty","bird",37,"usa")
user3=User("anna liza","kitting",45,"africa")
user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
user3.greet_user()
user3.describe_user()
