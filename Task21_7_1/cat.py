class Cat:
    def __init__(self, name = '', gender = '', age = -1):
        self.name = name
        if gender == 'm' or gender == 'g':
            self.gender = gender
        else:
            self.gender = ''
        if isinstance(age,int):
            self.age = age
        else:
            self.age = -1

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age