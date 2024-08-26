
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction,is_engine_started):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=bool(is_engine_started)

    def start_engine(self):
        self.is_engine_started=True
    def stop_engine(self):
        self.is_engine_started=False
        
    


def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3,is_engine_started=False)
    print(car.is_engine_started) 
    car.start_engine() 
    print(car.is_engine_started)
    car.stop_engine() 
    print(car.is_engine_started)

	
default_test()