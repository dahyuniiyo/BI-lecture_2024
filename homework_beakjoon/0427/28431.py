a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

data = [a, b, c, d, e]

for i in data:
    if data.count(i) == 2 or data.count(i) == 4:
        pass
    else:
        print(i)
