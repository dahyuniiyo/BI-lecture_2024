c = str(input())
n = int(input())

cnt = 0

for i in range(1, n + 1):
    re = str(input())
    if re[0:5] == c[0:5]:
        cnt += 1
    else:
        continue


print(cnt)
