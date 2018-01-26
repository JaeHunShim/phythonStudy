#튜플을 이용한 함수의 리턴값
list=[1,2,3,4,5]

for i,v in enumerate(list): #인덱스번호와 값을 동시에 가져옴
    print('{}번째 값:{}'.format(i+1,v))

print('---------------------------------------')
#튜플을 이용하게 되면
#말로 써보면 처음에 튜플에는 (0,1)이 들어가있을것임 그럼 이 튜플에서
#a[0]= 0 a[1]= 1이 되서 출력되고  이제 두번째 반복이 돌때는 튜플의 구성은
#(1,2) 이렇게 되있을거야 ~ 이제 이해가 되지
for a in enumerate(list):
    print('{}번째 값:{}'.format(a[0], a[1]))
print('-----------------------------------------')
#또는  (*) 슬라이싱 한다는 소리
for a in enumerate(list):
    print('{}번째 값:{}'.format(*a))
print('-----------------------------------------')

#튜플 딕셔너리 활용

ages = {'tod':35,'jane':23,'jae':20}

for key,value in ages.items():
    print('{}의 나이는:{}'.format(key,value))
print('-----------------------------------------')

#튜플을 사용하게 되면..
for key in ages.items():
    print('{}의 나이는:{}'.format(key[0],key[1]))
