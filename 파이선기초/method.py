class Human():
    '''인간'''
    def create_human(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print('{}이가  먹어서{}kg 이 되었습니다.'.format(self.name, self.weight))


    def walk(self):
        self.weight -= 0.1
        print('{}이가 걸어서 {} kg이 되었습니다.'.format(self.name, self.weight))

    def speak(self,message):
        print(message)

person = Human.create_human('재훈',40)

person.walk()
person.eat()
person.walk()
person.speak("안녕하세요")


class Car():
    '''자동차'''
    def run(self):
        print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name="택시"
taxi.run()
