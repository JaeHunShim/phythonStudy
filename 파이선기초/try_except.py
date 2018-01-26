#예외처리

def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{}의 index의 갑을 가지고 올수 없습니다.'.format(index))

safe_pop_print([1,2,3,6,8,9],5)

list = [1,2,3,4,5,6,7,8,9]

print(list.pop(3))

print(list)
## except 에러 연습

try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 무슨에러가 날지 모를대 가명으로
try:
    list = []
    print(list[0])
except Exception as e:
    print(e)

# 일부러 사용자가 에러를 발생시키는 경우 (raise)
print('------------------------------------------')
def rsp(mine,yours):
    allowed =['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try:
    rsp('바위','주먹')
except:
    print('잘못낸거 같습니다.')

#raise 연습
print('---------------------------------------------')
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
# 한곳만 나오게 해보기 현재는 2군데가 나옴
#(raise StopIteration)써서 강제 스톱 시키기
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
except:
    print("정상종료 되었습니다.")