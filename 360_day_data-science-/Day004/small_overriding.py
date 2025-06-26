 # overriding
class Employe:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Name:{self.name} \nsalary:{self.salary}")

class Developer(Employe):
    def __init__(self,name, salary, programming_language):
        super().__init__(name, salary) # overriding
        self.programming_language = programming_language
    
    def display_info(self):
        super().display_info()  
        print(f"Programming Language: {self.programming_language}\n")
class Manager(Employe):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # overriding
        self.team_size = team_size
    
    def display_info(self):
         super().display_info()  
         print(f"team_size: {self.team_size}")

developer = Developer(" Alice", 90000,"python")
manger = Manager("Bob", 120000, 5)

developer.display_info()
manger.display_info()