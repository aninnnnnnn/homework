# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.


class Transport:
    speed = 220
    fuel = 17
    price = 25000
    run = 12000

    def __init__(self, type, model, doors):
        self.type = type
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"Car: ({self.type}, {self.model}, {self.doors} doors)"

    @staticmethod
    def engine_on():
        print("WroomWroom")

    @classmethod
    def show_speed(cls):
        print(f"Car speed is {cls.speed}")

    @classmethod
    def show_fuel_perkm(cls):
        print(f"Fuel per km is {cls.fuel}")


    def car_model(self):
        print(f"Car model is {self.model}")

    def car_doors(self):
        print(f"Car has {self.doors} doors")

car1 = Transport("Sedan", "Porsche", 2)
car2 = Transport("Sedan", "Audi", 4)
car3 = Transport("Truck", "Toyota", 4)
car4 = Transport("Bus", "Ford", 2)
car5 = Transport("Sports", "Ferrari", 0)

print(car1)
car1.car_model()
car1.car_doors()
car1.show_fuel_perkm()
car5.engine_on()
print(car5.model)
print(car2.doors)

car5.speed = 300
print(car5.speed)

Transport.airbag = True
print(Transport.airbag)