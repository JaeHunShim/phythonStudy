#override: 쉽게 말하면 부모 클래스의 이름을 똑같은 이름으로 메소드를 덮어쓴다는 말임
#여기서는 해당 메소드를 그대로 받아서 메소드의 기능을 바꾸는 것을 override라고 한다.
class Animal():
    def walk(self):
         print ('걷는다')
    def eat(self):
         print('먹는다')
    def great(self):
        print('인사한다.')
class Cow(Animal):
    '''소'''

class Human(Animal):
    def wave(self):
        print('손을 흔든다.')
    def great(self):
        self.wave()

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다.')
    def great(self):
        self.wag()

person = Human()
person.great()

dog = Dog()
dog.great()

cow = Cow()
cow.great()

class Car():

    def run(self):
        print("차가 달립니다.")


class Truck(Car):

    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.
    def run(self):
        print('트럭이 달립니다.')

truck = Truck()
truck.run()