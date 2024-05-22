"""
def make_gugu(num):
    for i in range(2, 101):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")


make_gugu(1)  # 질문 : 아무 숫자나 넣어도 2단부터 100단까지 출력, num의 역할?
"""


# 자동화
def make_gugu_txt(num):
    with open(f"gugu_{num}_result.txt", "w") as handle:
        for i in range(1, 10):
            handle.write(f"{num} x {i} = {num*i}\n")


for i in range(1, 101):
    make_gugu_txt(i)
