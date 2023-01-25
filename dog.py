class dog:
    def __init__(self,Name,age,coatcolour):
        self.Name=Name
        self.age=age
        self.coatcolour=coatcolour
    def description(self):
            print(self.name,self.age)
    def get_info(self):
           print(self.coatcolour)

obj=dog(Name="puppy",age=5,coatcolour="Black")
class JackRussellTerrier(dog):
    def print(self):
        print("i am dog")
    def print(self):
        print("JackRussel")
class Bulldog(dog):
    def print(self):
        print("dog")
