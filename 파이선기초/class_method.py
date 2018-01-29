class Human():
    '''인간'''
    def __init__(self,name,weight): # 인스턴스를 만들때 실행되는 함수
        '''초기화 함수'''
        print("___init___실행")
        self.name = name
        self.weight = weight
    def __str__(self): #인스턴스가 문자열로 어떻게 출력될지 정해줌
        '''문자열화 함수'''
        return '{}몸무게 {}kg'.format(self.name,self.weight)


person = Human('재훈',50)
print(person.name)
print(person.weight)
print(person)