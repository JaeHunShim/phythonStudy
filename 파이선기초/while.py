# while문 사용해보기(if조건과 for문을 합친거랑 비슷)
selected = None

while selected not in ['가위','바위','보']:
    selected = input('가위 바위 보 중에 선택하세요>>>')

print('당신이 선택한 값은:', selected)

#while문 실습
numbers = [1,2,3]
length = len(numbers)
i = 0
while i<length :
    print(numbers[i])
    i = i + 1
# 위에있는걸 for문으로 바꾸면
print('------------------------------------')
for i in range(len(numbers)):
    print(numbers[i])