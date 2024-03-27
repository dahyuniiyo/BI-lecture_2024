"""
import random

# 정수의 개수 입력
count = int(input("생성할 정수의 개수를 입력하세요: "))

# 랜덤 정수 생성 및 출력
print("랜덤한 정수들:")
for _ in range(count):
    random_integer = random.randint(1, 100)  # -100부터 100 사이의 랜덤한 정수 생성
    print(random_integer, end=" ")
"""

cnt = 0
_ = input()  # 변수 명이 없는 변수..?
data = input().split()
v = input()
for elem in data:
    if elem == v:
        cnt += 1
print(cnt)
