#딕셔너리 반복문(딕셔너리의 경우는 값을 차례대로 뽑아오질 않는다)

#list의 경우

season=['봄','여름','가을','겨울']

for i in season:
    print(i)


#딕셔너리의 경우(키값을 가지고올때는 .keys()  값을 가지고올대는 .values() 사용)

age={'재훈':20,'주한':21,'영서':22}

print(age)

for key in age.keys(): #keys()는 생략이 가능하다 
    print(key)

print()

for value in age.values():
    print(value)

print()
for key in age:
    print(key)

for key,value in age.items(): # list 의 enumerate와 같은 기능
    print('{}이 나이는 {} 입니다'.format(key,value))

print()

for key in age:
    print('{}이 나이는 {} 입니다'.format(key,age[key]))
