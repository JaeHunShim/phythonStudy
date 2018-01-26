# 튜플 만들기 (튜플은 그냥 ( )로 만들어준다.안해줘도 대긴함
#튜플은 list처럼 순서가 정해져 있지만 안의 데이터 값을 변경할수는 없다.

tuple1=1,2,3
print(type(tuple))

tuple2=(1,2,3)
print(type(tuple))

list = [3,4,5]

tuple3= tuple(list)

#packing과 unpacking (하나의 변수에 여러개의 값을 넣는것)
#1. unpaking  즉 , c의 튜플의 값을 unpacking해서 a,b에 각각 대입
c = (3,4)
a,b = c
print(c)
print(a)
print(b)
#2. packing 즉, a, b 의 값을 가지고 d라는 튜플을 만들었다는 의미.
d= a,b
print(d)
# pack과 unpack의 장점 (서로 값을 바꿀때)
# 일반적인 방법으로 바꿀때(체인지 변수를 하나 가지고 왔다갔다)
x=5
y=10
temp= x
x= y
y= temp
print(x,y)
# 튜플을 사용했을시
c=x,y
d=y,x
print(d) #이런식으로 반대로 뽑아 올수 있다.
x,y= y,x
print(x,y)

def function():
    return 1,2

x,y= function()

print(x,y)
