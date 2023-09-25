class vehicle:    
    def __init__(self,make:str, model:str, mileage:int) -> None:
        self.make = make
        self.model = model
        self.mileage = mileage
        self.engine = "OFF"

    def get_details(self)-> None:
        print(f"The car make is {self.make} and model is {self.model}")
        print(f"Status of the engine is {self.engine}")

    def engine_run(self)-> None:
        self.engine = "ON"
        print(f"Now the engine is {self.engine}")

    def engine_stop(self)->None:
        self.engine = "OFF"
        print(f"Now the Engine is {self.engine}")


Ford = vehicle("Ford", "Fiesta", 28)
Benz = vehicle("Mercedes", "G-Wagon",10)

def addnumbers(num1:int, num2:int):
        print(f"Sum of numbers is {num1 +  num2}") 

if __name__ == "__main__":
    print(Ford.get_details())
    print(Ford.engine_run())
    print(Ford.engine_stop())
    addnumbers(1,2)
