#class와 intstance 의 이해
# 클래스: 함수나 변수들을 모아놓은 집합체
# 더 쉽게 말하면 instance들을  가지고있는 컨테이너의 역할이 클래스이다.
# 인스턴스; 클래스에 의해 생성된 객체이다.
#인스턴스는 각자 자신의 값을 가지고 있다.
number =[]
print(type(number))

number2 = list(range(10))
print(number2)

charactor = list("Hello")
print(charactor)
print(type(charactor))

print(isinstance(charactor,list))