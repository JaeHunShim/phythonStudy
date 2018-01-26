#break 문과 continue
"""
break문은 원하는값을 돌출한후 멈추고 싶을때 사용하면 좋음
continue는 직역해서 해석하면 게속 돌리라는 소리임
"""
sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
	if size == 32:
		print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
		break


# 여기서 보면 원래 if문을 나가야 하지만 if문을 끝내지 않고
# continue 처리를 해서 for문이 끝날때까지 게속 if문이 수행됨
numbers = [ (1,2),(10,0) ]

for a,b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a,b,a/b))