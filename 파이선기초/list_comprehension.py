#파이선의 list처리를 쉽게해주는 comprehention기능

areas = []

for  i in range(1,11):

    if i%2 ==0:
        areas = areas+[i*i]
print(areas)

# 더 간단한 방법
# for문을 돌면서 원하는 값을(i * i)반복해서 리스트에 넣어줄수가 있다.
areas2 = [i*i for i in range(1,11) if i%2 ==0]
print(areas2)
# 1부터 100사이의 8의 배수를 가지도록 리스트 만들기
list1 = [i for i in range(1,99) if i%8==0]
print(list1)

# 중첩듀플도 이렇게 할수 있다.
print([(x,y) for x in range(15) for y in range(15)])

list3 = [x for x in range(1,100) if x % 8==0]
print(list3)

#Dictonary을 comprehension 으로, 처리해보기
students = ['재훈','주한','영서','엄마','아빠']
#일반적인 방법으로 리스트를 딕셔너리로 만들기
for number, name in enumerate(students):
    print(number+1,name)
#comprehension 을 사용하면
students2 = {'{}번째'.format(number+1):name for number,name in enumerate(students)}
print(students2)
# 두개의 리스틀 합쳐서 하나의 딕셔너리로 만들어보기
score = [23,45,67,78,89]
for x,y in zip(students,score):
    print(x,y)
#위에걸 딕셔너리를 이용해서 하면

score2 = {student:scores for student,scores in zip(students, score)}

print(score2)

#예제
product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {product:price for product,price in zip(product_list,price_list)}

print(product_dict)

