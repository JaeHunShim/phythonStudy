class Human():
    ''' 사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = '영어'

person1.name = '서울사람'
person2.name = '미국인'

def speak(person):
    print('{}이{}로 말하고 있습니다.'.format(person.name, person.language))


Human.speak = speak

person1.speak()
person2.speak()
