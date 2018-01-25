#list (리스트의 값 추가하기 append를 사용하든지 새로운 리스트를 만들면서 추가하는 방법이 있다)
#list의 특정 위치를 지울때는 del list[원하는위치]
#list의 특정 값을 지우고 싶을때는  리스트이름.remove(지우려는 데이터값)
#in 은 원하는게 있는지 없는지 boolean 타입으로 알려고 할때 사용하면 유용

list2 = [10 , 20 , 30 , 40, 56 ,69]

print(list2)

#list2.append(50)  #리스트에 값을 추가 시키는방법

#print(list2)

list3 = list2+[70] #새로운 리스트에 리스트를 담아서 사

print(list3)

list4 = list2+list3 #리스트더해서 새로운 리스트를 만들수도 있음 

print(list4)

n = 100

truefalse = n in list4  # in함수는  안에 값이 있는지 확인하는 용도로 사용할수 있다.

print(truefalse)

if n in list4:
    print('{} 이 {}에 있습니다'.format(n,list4))
else:
    print('{} 이 {}에 없습니다'.format(n,list4))

del list4[10] #특정위치의 리스트값을 지움
print(list4)

list4.remove(69) #리스트의 특정값을 지울수도 있다.
print(list4) 
