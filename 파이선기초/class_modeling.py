class Human():
    '''인간'''
'''
person = Human()
person.name = '철수'
person.weight = 70
'''

# 함수를 하나 정의해놓고
def create_human(name, weight):
    person = Human() # person이라는 insance 생성
    person.name = name  # 매개변수의 값을 그대로 instance에 활용
    person.weight = weight
    return person
# 해당함수를 Human클래스의 하나의 인스턴스로 만들어서
Human.create = create_human
# 해당인스턴스를 하나의 변수에 저장한다.
person = Human.create('재훈',40)

# eat함수는 파라미터로 해당 인스턴스를 받아서 즉 Human.create가 들어있는 person을 ~
def eat(person):
    person.weight +=0.1
    print('{}이가  먹어서{}kg 이 되었습니다.'.format(person.name,person.weight))
# 걷는 함수도 마찬가지
def walk(person):
    person.weight -=0.1
    print('{}이가 걸어서 {} kg이 되었습니다.'.format(person.name,person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()




