
# 상속: 중복되는 코드를 줄이기위해서 사용함

class Animal():
     def walk(self):
         print ('걷는다')
     def eat(self):
         print('먹는다')

class Human():
    def wave(self):
        print('손을 흔든다.')

class Dog():
    def wag(self):
        print('꼬리를 흔든다.')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()