#리스트의 다양한 기능 활용해보기

list1 = [123,456,78,657,234]
#특정한 인덱스의 위치를 알려줄때 .index
print(list1.index(456))
#없는 값을 넣으면 오류가 난다. ValueError
#print(list1.index(57))

print(50 in list1) #먼저 검사하고

if 50 in list1:
    print(list1.index(50))

#list끼리 서로 붙이는 함수 extend
#일반적인 방법

list2 = [1,2,3] + [4,5,6]
print(list2)

#extend 활용

print(list1)
list1.extend([4,5,6]) #추가 된걸 확인할수 있다.
print(list1)

#insert 특정한값을 원하는 인덱스 위치에 넣어줄수 잇다
print(list1)

list1.insert(-1,9999)
print(list1)

#list1.insert(888)
#print(list1)

#sort 순서대로 정렬해서 나오게 함 올림차순
list1.sort()
print(list1)
#inverse 역순으로 뽑아모 내림차순

list1.reverse()
print(list1)

# 특정인덱스에 값이 있으면 인덱스 위치를 반환하고 아니면 None반환
def safe_index(my_list,value):
    if value in my_list:
        return my_list.index(value)
    else:
        return None



#########################################
list1 = [1,2,3,4]

list1.extend([5,6,7,9])
print(list1)
list1.insert(0,8)
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)