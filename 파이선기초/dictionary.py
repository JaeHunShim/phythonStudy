# 딕셔너리 만들기(키값으로 원하는 value 값을 가지고 오는 방법 JSON형태
# 가져올대는 ()가 아니라 list 에서 가지고 온 방법처럼 []를 사용해서 가져옴
# 여러 값을 저장해두고 필요한 값을 꺼내쓰는 기능 
winTable={
    '가위':'보',
    '바위':'가위',
    '보':'바위'}

print(winTable['가위'])


#가위, 바위, 보 만들어보자



def rsp(me,you):

    if me == you:

      return 'draw'

    elif winTable[my]== you:

       return 'win'

    else:

       return 'lose'


n=rsp('바위','보')

print(n)

message = {

    'draw':'비김',
    'win':'이김',
    'lose':'짐'

    }

print(message[n])
