#논리연산에 대해서 더 알아보기

def return_false():
    print('함수는 항상 False')
    return False

def return_true():
    print('함수는 항상 True')
    return True

print('테스트1')
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

print('테스트2')
# 앞에처음부터 False이기때문에 뒤에무엇이 와도 False기 때문에 출력
# 결과물이 하나 더 안나오는거징
if return_false() and return_true():
    print(True)
else:
    print(False)

