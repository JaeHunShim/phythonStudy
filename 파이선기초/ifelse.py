# if else 문 (조건이 거짓일때 else문 실행) 가위바위보 만들어보기

gawi = "가위"
bawi = "바위"
bo = "보"

win = "이김"
draw = "비김"
lose = "짐"


mine="보"
your="바위"


if mine == your:
    result = draw
else:
    if mine==gawi:
        if your==bawi:
            result=lose
        else:
            result=win
    elif mine==bawi:
        if your==gawi:
            result=win
        else:
            result=lose
    elif mine==bo:
        if your==gawi:
            result=lose
        else:
            result=win
    else:
        print("제대로내라")

print(result)
    
