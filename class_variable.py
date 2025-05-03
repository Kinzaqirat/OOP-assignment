class Bank:
    bank_name="123 bank"

    def __init__(self,customer):
        self.customer=customer
    def display_info(self):
        print(f"Customer: {self.customer}, Bank: {Bank.bank_name}")    
    @classmethod
    def change_name(cls,name):
        cls.bank_name=name

name=Bank("Joesp")
name.display_info()
Bank.change_name("ABC")
name.display_info()