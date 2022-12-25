# Assignment-6
import json
dict={"Uttar Prashesh": "Lucknow","Bihar": "Patna","Himachal Pradesh": "Shimla","Telangana":"Hyderabad","Punjab": "Chandigarh","Madhya Pradesh":"Indore","Rajasthan": "Jaipur"}
json_object= json.dumps(dict,indent=4,separators=(",","="))
print(json_object)





import json

class Employees:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open (r"C:\Users\admin\Desktop\Empolyees.json") as file:
    data= json.load(file)
    print(data)

employees = [Employees(e['Name'], e['DOB'], e['Height'], e['City'] , e['State']) for e in data['Employees']]

for employee in employees:
    print("Name: ", employee.name) 
    print("DOB: ", employee.dob) 
    print("Height: ", employee.height) 
    print("City: ", employee.city) 
    print("State: ", employee.state) 
    print("\n")

# class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        print (f"{self.name} is {self.age} years old")

    def get_info(self):
        print (f"Tim has {self.coat_color} coatcolor")

dog1=Dog('Tim',7,'White')

dog1.description()
dog1.get_info()

class JackRussellTerrier(Dog):
    def mycity(self):
        print("texas")

    def favsnack(self):
        print("peddigree")

class Bulldog(Dog):
    def mycity(self):
        print("frankfurt")
    def favsnack(self):
        print("meatballs")

jack=JackRussellTerrier("alan",5,"red")







       




