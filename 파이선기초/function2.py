# 함수 만들어보기2 (매게변수사용하기)

def print_root(a,b,c): # 함수 옆에 있는 괄호안의 파라미터를 매개변수

    r1= a+b
    r2= a+b
    r3= (a+b)*c

    print(r1,r2,r3)

x=2
y=2
z=5

print_root(x,y,z) #실행되는 값을 실행인자 argument라고 한다. 


def print_round(number):

    rounded=round(number)
    print(rounded)

#매개변수와 실행인자의 파라미터의 갯수를 일치 시켜야 한다. 
print_round(4,6)
print_round(2,2)


