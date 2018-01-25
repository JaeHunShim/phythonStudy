#for문(for in list)  - 순회할 리스트가 정해져 있을때 사용하면 좋음 

patterns=[1,2,3,4,5,6,7,8,9,10]

for i in patterns: #pattern의 값을 순서대로 하나식 꺼내와서 i에 하나씩 넣으면서 반복문이 돌아감 
    print(i)

print()

#for문(for in range) - 원하는 횟수만큼 반복 - 반복할 횟수가 정해져 있을때 사용하면 좋음 
#range 원하는 횟수만큼 뽑아옴 가령 for i range(4) 4번 반복해서 뽑아오는 의미
#len list길이만큼 반목해서 뽑아온다 가령 for i ren(배열변수))  이런식으로 하면 그만큼만 뽑아옴
#enumerate 순서와 리스트 값을 모두 만들어 낼수 있음 

for i in [0,1,2,3,4,5]:  #만약 100개를순서대로뽑을꺼면 이런식은 개노가
    print(i)

print()

for i in range(5): #이런식으로 사용하면 쉽게뽑아올수 있지 
    print(i)


name=['영희','철수','미애','재훈','주한']

for i in range(len(name)):
    names = name[i]
    print('{}번:{}'.format(i+1,names))

print()

for i,names in enumerate(name): # 여기서 i 0부터 증가하는 횟수 names는list안에 있는 name이 하나씩 대입되는 데이터 
    print('{}번:{}'.format(i+1,names))
