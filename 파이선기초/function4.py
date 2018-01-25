# 함수 만들어보기4(return)
# return 은 그값을 반환하고 함수를 끝내겠다는 소리임 

def add(value):

    if value < 10:

        return 10,20 # 이렇게 특정조건때 return하여 끈낼수도 있고  return을 두개로  할수도 있다.

    result = value+10

    return result

a= add(4)

print(a)

a = add(20)

print(a)

