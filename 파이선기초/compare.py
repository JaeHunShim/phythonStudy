# 딕셔너리와 리스트의 비교
list = [1,2,3,4,5,6]
dict = {'one':1,'two':2}

print(list[0])  # 리스트 0번재 값

del list[0] # 리스트 0번째 값 삭제
del dict['one'] # 딕셔너리 one의 값

print(list)
print(dict)

list.clear() # 모두 삭제
dict.clear()

print(list)
print(dict)

#딕셔너리와 리스트에 값추가 해보기

list=[1,2,3,4,5,]
dict={1:100,2:200,3:300}
list2=[2,5,6,7]

list3=list+list2
print(list3) # 모두 출력되는걸 볼수 있음
dict2={1:200,4:400}
dict2.update(dict)# 동일한 키값이 있으면 대체하는 걸 볼수 있다.
print(dict2)


#예제 연습(키값이 불량품일때 딕셔너리 비우기)
def check_and_clear(i):
    if '불량품' in i:
        i.clear()
        print('불량품입니다.')

    else:
        print(i)


box={'불량품':' 상자'}

check_and_clear(box)

#딕셔너리 업데이트 해보기
products = {"풀":800, "딱풀":1200, "색종이":1000,"색연필":5000,"스케치북":3500}

catalog = {"겨울용 실내화":12000, "잠자리채":8000, "딱풀":1400}


products.update(catalog)

print(products)
