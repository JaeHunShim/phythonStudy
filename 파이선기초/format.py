#문자열.format(format은 문자열 처리를 쉽게 해주는 방식이다 주의할점은 {}와 변수의 갯수가 동일해야)
                #원하는 값을 출력할수 있

number = 20
getting = '안녕하세요'
place='포맷한번 해보겠습니다'
welcome='어서오세요'

#예전 방식

print(number,'번째 손님',getting,'.제가한번' ,place ,welcome,'!')

# 문자열 format사용하기 {}를 사용하는데  {}의값을 순서대로 넣어주는 역할을 해준다. 

base ='{} 번째 손님 {} .제가한번 {} {} !'

new_way = base.format(number,getting,place,welcome)

print(base)
print(new_way)

mine='가위'
your='바위'
result='졌다'

print('나는 {} 너는 {} 그래서 {}'.format(mine,your,result)) #이런식으로 사용할수도 있음 
