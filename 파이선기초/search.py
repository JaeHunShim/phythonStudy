#검색하는 방법

"""
1. 검색은 무조건 google.com 에서 해야한다
2. 검색 키워드에는 키워드에 무조건 "파이선3"을 넣어라
3. 코드를 포함한 글을 찾도록 하자
4. 간단한 예제는 REPL을 사용해서 해보자
5. 영어를 못해도 영어로 검색하자 


"""
#영어로 검색해서 현재 시간 얻어오기
import datetime
now = datetime.datetime.now()

print(now)

print(now.strftime("%y,%m,%d"))

print(now.year ,now.month, now.day)


#문서찾기

"""
공식문서 찾기: 검색하고자 하는 내용 다음 site:python.org 를 넣어주면된다.
그럼 해당 사이트의 공식문서만 보여줌 예로 site:stackOverflow.com 이렇게 하면 해당사이트에 대한것만 보여

"""

