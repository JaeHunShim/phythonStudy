# 평균 구해보기

def average(list):
    total =0
    for i in range(len(list)):
        total = total+list[i]
        i = i+1
    return total/i

list1 = [2,4,6,8,10]
print(average(list1))

# 랜덤 함수로 무조건 ture나오게 하기
from random import randint
class lucky(object):
    def __eq__(self,other):
        return True

def maybe_lucky(lucky1,lucky2):
    lucky1 = lucky()
    lucky2 = lucky()
    if lucky1 ==lucky2:
        return True


print(maybe_lucky(400,100))


def maybe_lucky():
    while True:
        number= input("숫자를 입력해주세요")
        number2= randint(0,100)
        if int(number)==number2:
            print('당신이 입력한 숫자{}와 {}가 일치합니다.'.format(int(number),number2))
            break
        else:
            number2 = randint(0,100)
            print(number2)
            print("다시 입력해주세요")

maybe_lucky()