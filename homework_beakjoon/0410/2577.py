A = int(input())
B = int(input())
C = int(input())
D = A * B * C

data = str(D)
# 리스트 안해도 됨

for i in range(10):
    print(data.count(str(i)))

"""
print(data.count("0"))
print(data.count("1"))
print(data.count("2"))
print(data.count("3"))
print(data.count("4"))
print(data.count("5"))
print(data.count("6"))
print(data.count("7"))
print(data.count("8"))
print(data.count("9"))

# 질문 : 반복문 사용해서 표현
# for i in range(10)

data = dict()

for i in D:
    if i not in data:
        data[i] = 0

    data[i] += 1

print(data)

for i in range(0, 10):
    print(data.get(str(i), 0), end="")


print(data["9"])
print(data.get)
"""
