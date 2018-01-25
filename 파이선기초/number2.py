#정수와 실수 


five1 = 5
five2 = 5.0
five3 = 5.000000

print(five1)    #5
print(five2)    #5.0
print(five3)    #5.0

five4 = 5 * 1
five5 = 5 * 1.0

print(five4)    #5
print(five5)    #5.0

division = 6 / 5
division2 = 6 // 5

print(division) #1.2
print(division2)    #1 (정수형으로 나타난다)

print(0.1 + 0.1)  #0.2
print(0.1 + 0.1 + 0.1) #0.30000000000000004 false 반환

# 이런식으로 정확하게 명시해 주는 방법이 좋을때도 있다
print(int(2.0))
print(float(5.2232424))
