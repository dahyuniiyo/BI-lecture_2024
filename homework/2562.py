"""
import random

random_number = random.sample(range(1, 101), 9)
print("아홉개의 숫자는 다음과 같습니다:", random_number)

max_value = random_number[0]

for num in random_number:
    if num > max_value:
        max_value = num

print(max_value)
"""

data = list()
for i in range(9):
    num = int(input())
    data.append(num)

max_num = max(data)
print(max_num)
print(data.index(max_num) + 1)

"""
max_num = 0
for i in range(9) :
    num = int(input())
    if num > max_num:
        max.num = num

print(max_num)

#주어진 수중에 가장
"""
