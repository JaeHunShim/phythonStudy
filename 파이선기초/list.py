#list (여러개의 앖을 하나의 변수에 모아놓은것)

list1 = ['가위','바위','보']
list2 = [10 , 20 , 30 , 40]

print(list1)
print(list2)

print(list1[2]) #인덱스의 위치는 0부터 시작 함
print(list2[1])

#리스트 안의 값을 바꾸어보기

list1[0]='가위바위보'

print(list1)

print(list2[-1],list2[-2])  #음수는 인덱스의 반대편에서 부터 가지고옴
