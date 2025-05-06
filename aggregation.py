class Employee:
    def __init__(self,name):
        self.name=name

    def get_details(self):
        return f"Employee Name {self.name}"     
class Department:
    def __init__(self,name,employee):
        self.name=name
        self.employee=employee

    def show_employee(self):
        return f"Department: {self.name} → {self.employee.get_details()}"

emp = Employee("Alice")        
dept = Department("HR", emp)    
print(dept.show_employee())      