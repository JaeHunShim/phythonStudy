#자식 클래스에서 부모의 클래스의 내용을 사용하고 싶을 경우 
# super()을 사용하면됨 즉, 부모의 메소드를 사용하고 싶을대 자식 메소드에서~
class Animal():
    def __init__(self,name):
        self.name = name
    def walk(self):
         print ('걷는다')
    def eat(self):
         print('먹는다')
    def great(self):
        print('{}이 인사한다.'.format(self.name))

class Human(Animal):
    def __init__(self,name, hand):
        super().__init__(name) ## 부모에서 넘겨져온 값만 처리해서 사용
        self.hand = hand
    def wave(self):
        print('{}을 흔들면서'.format(self.hand))
    def great(self):
        self.wave()
        super().great()

person = Human('사람','오른손')
person.great()


class Car():

    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    def __init__(self,capacity,name):
        super().__init__ (name)
        self.capacity = capacity
        print('{}톤{}이'.format(capacity,name))
    def load(self):
        print("화물을 싣고")
    def run(self):
        print('과속하고있습니다.')


myCar = Truck(2,'미친트럭')
myCar.load()
myCar.run()



