#문자열""와 ''의 사용법 (""안에는 ''안에 들어갈수 잇고 ''안에 ""들어갈수 있다.)
#긴 문자열을 사용할때는 '''(따옴표 3개를 사용해서 처리하면된다.

# 이런식으로 사용하면 안된다
"""
long_string='파이선 초보입니다
열심히 하고있습니다'
"""
#그래서 파이선은 ''' 로 긴 문자열을 처리할수 가 있다.
long_String2 ='''파이선을 배우고 있는 초보입니다
열심히 하고 어서 빨리 배우고 싶습니다'''

print(long_String2)

quote1 = '가끔은 "와'+'"을 같이 쓰기도 합니다.'

quote2 = '''가끔은 "와"을 같이 쓰기도 합니다.'''

print(quote1)
print(quote2)
