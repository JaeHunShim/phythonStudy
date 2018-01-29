#Slice 원하는 범위내의 데이터를 잘라서 가지고옴
#Slice를 이용해서 리스트를 복사하면 편하게 쓸수 있기때문에 많이 사용함
text = 'Hellow World'
print(text[2])
print(text[1:5])

list = ['영','일','이','삼','사']
print(list[1:3])
print(list[2:len(list)]) # 끝가지 얻어올수도 있아 len을 이용해서
print(list[:2])
print(list[:])

list1= [25,67,89,567,456]
list2 = list1[:]
print(list1)
list1.sort()
print(list1)
print(list2)

#예제
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[ :3 ]

print(red_colors)

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[ 4 : len(rainbow) ]
print(blue_colors)


def substring(str, start, end):
    str = str[2:5]
    return str


str = 'Hello World'
between_2_5 = substring(str,2,5)
print(between_2_5)
