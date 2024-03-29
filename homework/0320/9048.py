"""
# 문자열 입력 받기
string = input("문자열을 입력하세요: ")
string = string.replace(" ", "")

if string.isalpha() and string.isupper():
    first_character = string[0]
    last_character = string[-1]
    print(first_character + last_character)

else:
    while True:
        string = input("대문자 알파벳으로만 이루어진 문자열을 입력하세요: ")
        if string.isalpha() and string.isupper():
            first_character = string[0]
            last_character = string[-1]
            print(first_character + last_character)
            break
"""

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대하여 반복
for _ in range(T):
    # 문자열 입력
    string = input()

    # 첫 번째 글자와 마지막 글자 출력
    first_character = string[0]
    last_character = string[-1]
    print(first_character + last_character)
