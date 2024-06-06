# def decor1(func):
#     def inner():
#         x = func()
#         return x * 4
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return x - 10
#     return inner
#
# # @decor2
# @decor1
# def return_num():
#     return 5
#
# print(return_num())

#
# result = decor(return_num)
# print(result())

class Human:
    height = 170
    weight = 60

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @staticmethod
    def sleeping():
        print("ZZzzZZZZzzzzzzzzzzzz...")

    @classmethod
    def show_height(cls):
        print(f"Human Height is: {cls.height}")

    def say_hi(self):
        print(f"Hi, my name is {self.name}")

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human1 = Human("Nika", 19)
human2 = Human("Elene", 15)

print(human1)
print(human2)

# human1.name = "Nika"
# human2.name = "Elene"
# human1.say_hi()
# human2.say_hi()



# human1.show_height()
# human2.show_height()
# print(human1.name)
# print(human2.name)

# Human.show_height()


# Human.hands_number = 2
#
# print(Human.hands_number)
#
# Human.sleeping()
