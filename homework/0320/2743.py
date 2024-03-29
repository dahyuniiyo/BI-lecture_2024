while True:

    string = input("알파벳으로 이루어진 문자열을 입력하시오: ")

    length = len(string)

    if length > 100:
        print("10자 이하의 문자열로 다시 입력하시오: ")

    elif any("ㄱ" <= char <= "힣" for char in string):
        print("알파벳으로 이루어진 문자열로 다시 입력하시오: ")

    else:
        print(length)
        break
"""

def get_valid_input():
    string = input("알파벳으로 이루어진 문자열을 입력하시오: ")
    length = len(string)

    if length > 10:
        print("10자 이하의 문자열로 다시 입력하시오.")
        return (
            get_valid_input()
        )  # 조건을 만족하지 않으면 함수를 재귀적으로 호출하여 다시 입력 받음
    elif any("ㄱ" <= char <= "힣" for char in string):
        print("알파벳으로 이루어진 문자열로 다시 입력하시오.")
        return (
            get_valid_input()
        )  # 조건을 만족하지 않으면 함수를 재귀적으로 호출하여 다시 입력 받음
    else:
        return length


result = get_valid_input()
print(result)
"""


print(ord("A"))  # 65
print(ord("Z"))  # 65
print(ord("a"))  # 65
print(ord("z"))  # 65

word = input()
for char in word:
    if ord("A") <= ord(char) <= ord("2"):
        flag = True
    else:
        print(char, "is not alphabet")
        flag = False
        break
