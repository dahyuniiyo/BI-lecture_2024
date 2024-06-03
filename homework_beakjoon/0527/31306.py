A = str(input())

cnt1 = 0
cnt2 = 0

for i in A:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cnt1 += 1
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
        cnt2 += 1

print(cnt1, cnt2)
