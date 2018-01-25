# if 문 Block
# 들여쓰기가 어긋나면 오류가 난다.내부블럭은 외부블럭에 종속적이다
if True:
    print("블록이 속한 코드")
    if False:
        print("한줄더")
    if True:
        print("또한줄더")

print("이건 다른거")

# 첫번째 블락이 False니까 그 블럭안에 있는 모든 함수들이 다 False라서 마지막 print만 출
if False:

    print("If 첫번째")

    if True:
        print(" if 두번재")
        if True:
            print("if 세번째")

print("if 네번째")
