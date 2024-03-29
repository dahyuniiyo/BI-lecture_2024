"""
import sys

input_rule = input("0 < a,b < 10")

while True:
    input_a = input("정수 a를 입력하세요:")

    input_b = input("정수 b를 입력하세요:")

    if (
        int(input_a) > 0
        and int(input_a) < 10
        and int(input_b) > 0
        and int(input_b) < 10
    ):

        print(int(input_a) + int(input_b))
        break

    else:
        print("유효한 범위의 값을 입력하시오:")
"""

s = input()
num1, num2 = s.split()
result = int(num1) + int(num2)
print(result)
