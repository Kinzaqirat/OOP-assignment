class Employee:
    def __init__(self,name,salary,ssn):
        self.name=name
        self._salary=salary
        self.__ssn=ssn

emp = Employee("Alice", 75000, "123-45-6789") 
print(f"Name: {emp.name} (public)")
print(f"Salary {emp._salary} (protected)")       

try:
    print("Private (__ssn):", emp.__ssn) 
except AttributeError as e:
    print("Private (__ssn): Cannot access directly:", e)