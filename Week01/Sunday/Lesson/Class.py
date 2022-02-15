class Nurtay:

    def __init__(self, age, gender, sound):
        self.age = age
        self.gender = gender
        self.sound = sound
 
    def getSound(self):
        return self.sound

    def printSound(self):
        print(self.getSound())

    def f1(self):
        return self.age
    
    def f2(self):
        print(self.f1())


class Table:

    def __init__(self, _nogi, _vid, _width, _height):
        self.nogi = _nogi
        self.vid = _vid
        self.width = _width
        self.height = _height

    def CalculateArea(self):
        return self.height * self.width
    
    def printArea(self):
        print(self.CalculateArea())

    def setHeight(self, newHeight):
        self.height = newHeight

# newPerson = Nurtay(18, 'Male', input())
# PersonSecond = Nurtay(25, 'Female', input())

# newPerson.printSound()
# print(PersonSecond.getSound())
# print(newPerson.f1())
# print(PersonSecond.gender)

newTable = Table(4, 'derevo', 2, 3)

newTable.setHeight(int(input()))

newTable.printArea()
# атрибуты - переменные
# методы - функции

