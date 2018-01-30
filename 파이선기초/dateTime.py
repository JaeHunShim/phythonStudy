#dateTime 사용해보기
import datetime
print(datetime.datetime.now())

startDateTime = datetime.datetime.now()
print(type(startDateTime))
#날짜 바꾸기
start_time = startDateTime.replace(year=2016,month=2 ,day=1)
print(start_time)

start_time = datetime.datetime(2018,4,23)
print(start_time)

#남아있는 시간 알아보기
nam = start_time - datetime.datetime.now()
print('4월 23일 까지는 {} 일{}시간이 남았습니다.'.format(
    nam.days,nam.seconds
))
# 현재시간에서 100일후는 언제인가
# 현재시간에서 100일전은 언제인가
# 내일 10시 지정해보기
# 다른 클래스들끼리 더하고 뺄수 있다.
hundred = datetime.timedelta(days = 100)
hundredAfter = datetime.datetime.now()+hundred
hundredBefore = datetime.datetime.now() - hundred
tommrrow = datetime.datetime.now().replace(hour=10 ,minute=0,second= 0)
print('지금부터 100일후는 {}입니다.'.format(hundredAfter))
print('지금부터 100일전은 {}입니다.'.format(hundredBefore))
print('내일 10 시는 {}입니다.'.format(tommrrow))

# 지금보다 100일전은 언제인가
# hundred2 = datetime.timedelta(days = -100)
# hundredBefore = datetime.datetime.now() + hundred2
# print(hundredBefore)

after = datetime.timedelta(days =100)
hundred1_after = datetime.datetime.now()+ after
hundred_after = hundred1_after.replace(hour = 7, minute=0,second=0,microsecond=0)

print(hundred_after)