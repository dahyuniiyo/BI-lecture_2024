N = int(input())
S = str(input())
cnt = 0

for char in S:
    if char in "aeiou":
        cnt += 1

print(cnt)
