#List Step
# Step 은 주어진 값만큼 뛰어서 가지고 오게 하는 기능이다.

list1 = list(range(20))
print(list1)

print(list1[5:15])

print(list1[5:15:2])
print(list1[5:15:3])
print(list1[15:5:-2]) # 리스트의 반대로 할수도 있음 대신에 거꾸로니까 end 값을 반대로 해주어야함
print(list1[::2])

#예제
list2 = list(range(20))
print(list2)
new_list = list1[5:15:3]
print(new_list)
reverse_list = list2[17:4:-4]
print(reverse_list)

#Slice로 list수정해보기

numbers = list(range(10))
print(numbers)

del(numbers[0])
print(numbers)

del(numbers[:5])
print(numbers)

numbers[1:3]  = [77,88,99]
print(numbers)
numbers[1:3] = [4]
print(numbers)

list4 = list(range(6))
print(list4)

list4[1:4] =[11,22,33]
print(list4)