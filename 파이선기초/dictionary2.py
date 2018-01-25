# 딕셔너리 update, remove (RUD)

#리스트의 경우

list=[1,2,3,4,5]

list[2]=33

print(list)

list.append(6)

print(list)

#딕셔너리의 경우

dictionary={'ong':1, 'two':2, 'three': 3}

print(dictionary)

dictionary['three'] = 22 ##값 바꾸기

print(dictionary)

dictionary['four']=4 #추가

print(dictionary)

del(dictionary['ong']) #삭제

print(dictionary)

print(dictionary.pop('three')) #결과값을 반환하면서 삭제 

print(dictionary)


