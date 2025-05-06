class Engine:
    def start(self):
        print("Engine started...")

class Car:
    def __init__(self,engine):
        self.engine=engine

    def start_car(self):
        self.engine.start()    


engine = Engine()
my_car = Car(engine)
print(my_car.start_car())
