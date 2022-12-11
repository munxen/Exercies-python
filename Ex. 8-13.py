#Profile: Start with a copy of the program user_profile.py . Create your own profile 
#by calling build_profile(), specify the first name, last name and three other key—value pairs for 
#of your description.

def build_profile(first,last,**other):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in other.items():
        profile[key]=value
    return profile
user=build_profile("Juriy","Orlov",age=20,country="Russia",city='Krasnodar')
print(user)