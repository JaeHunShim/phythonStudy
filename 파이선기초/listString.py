#list와 String과 비슷한기능

my_list = [2,3,4,5]
str = "Hello World"


# 리스트와 똑같이 해당 위치의 값을 뽑아올수 있다.
print(my_list[0])   # 2출력
print(str[0])   #"H"출력
print(str[3])   # "l"출력

# 리스트에 있는지 검색하는 기능도 똑같이 할수 있다.
print(3 in my_list) #True
print("o" in str)   #True

# 인덱스 위치를 알아보는 기능도 비슷하다

print(my_list.index(5)) #3출력
print(str.index("d"))  # 10 출력

#문자열을 list로 만들수도 있다.

characters = list("abcdef")
print(characters) # [a,b,c,d,e,f]

# str.sprit을 사용해서 문자열을 리스트로 바꿀수 있다.
words = "재훈이는 정말 열심히 하고있습니다."
words_list = words.split()
print(words_list) # ['재훈이는', '정말', '열심히', '하고있습니다.']

#split에 안에 파라미터 를 주면 그 파라미터를 기준으로 쪼개서 list로 만들어준다

time = "지금 시각은 10:20:45 초입니다."
time_list=time.split(":")
print(time_list) # ['지금 시각은 10', '20', '45 초입니다.']

# " ".join(list) 리스트를 다시 문자열로 바꾸기
print(" ".join(words_list))  #재훈이는 정말 열심히 하고있습니다.


str = "오늘은 날씨가 흐림"

words = str.split() # ['오늘은', '날씨가', '흐림']
print(words)

position = (words.index("흐림"))
print(position)  # 2
words[position] = "맑음" #흐림을 맑음으로 대체
print(words) # ['오늘은', '날씨가', '맑음']

new_str = " ".join(words)
print(new_str)