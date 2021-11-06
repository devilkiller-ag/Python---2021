class Animals:
    def __init__(self):
        print(f'An animal is born...')
    
class Pet(Animals):
    def __init__(self):
        super().__init__()
        print(f'This Animal is a Pet...')

class Dog(Pet):
    def __init__(self):
        super().__init__()
        print(f'This pet is an Dog!')

    @staticmethod
    def bark():
        print(f'Barking...Bhow..Bhow..')

puppy = Dog()
puppy.bark()