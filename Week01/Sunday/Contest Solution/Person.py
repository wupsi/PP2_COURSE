class Person:
    
    def __init__(self, _name, _surname, _age, _height, _weight):
        self.name = _name
        self.surname = _surname
        self.age = _age
        self.height = _height
        self.weight = _weight
        self.agePeriod = 'not set'
        self.gender = 'not set'
        self.bmiValue = 'not set'

    def setAgePeriod(self):
        if 13 <= self.age <= 17: self.agePeriod = 'teenager'
        elif 18 <= self.age <= 21: self.agePeriod = 'youth'
        elif 22 <= self.age <= 38: self.agePeriod = 'young'
        elif 39 <= self.age <= 60: self.agePeriod = 'adult'
        elif self.age >= 61: self.agePeriod = 'oldman'

    def getAgePeriod(self):
        self.setAgePeriod()
        return self.agePeriod

    def setGender(self, _gen):
        if _gen == 'M': self.gender = 'Male'
        elif _gen == 'F': self.gender = 'Female'

    def getGender(self):
        return self.gender

    def getBodyMassIndex(self):
        return self.weight / (self.height * self.height * 0.0001)

    def setWeightValue(self):
        bmi = self.getBodyMassIndex()
        if bmi < 18.5: self.bmiValue = 'underweight'
        elif 18.5 <= bmi <= 24.9: self.bmiValue = 'normal'
        elif 25 <= bmi <= 29.9: self.bmiValue = 'overweight'
        elif 30 <= bmi <= 34.9: self.bmiValue = 'obese'
        elif bmi >= 35: self.bmiValue = 'extremely obese'
            
    def getWeightValue(self):
        self.setWeightValue()
        return self.bmiValue


Persons = []
for i in range(int(input())):
    info = input().split()
    newPerson = Person(info[0], info[1], int(info[2]), int(info[3]), int(info[4]))
    if len(info) == 6: newPerson.setGender(info[5])
    Persons.append(newPerson)

for pers in Persons:
    print('------------------------------------')
    print(pers.name + "'s info:")
    print('Full name: ' + pers.name + ' ' + pers.surname)
    print(f'Age: {pers.age} years old\nAge period: {pers.getAgePeriod()}')
    print(f'Height and weight: {pers.height}cm and {pers.weight}kg')
    if len(info) == 6: print(f'Sex: {pers.getGender()}')
    print(f'Body Mass Index: {pers.getBodyMassIndex()}')
    print(f'Weight Value: {pers.getWeightValue()}')
