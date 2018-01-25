#모듈 사용해보기

#random.choice():무작위로 하나를 선택 하는 함수 

import random

candidate=['가위','바위','보']

for i in range(20):
    select= random.choice(candidate)
    print('{}번째는{}'.format(i+1,select))
