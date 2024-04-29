DNA = str(input())
cnt_A = 0
cnt_C = 0
cnt_G = 0
cnt_T = 0

for char in DNA:
    if char == "A":
        cnt_A += 1
    elif char == "C":
        cnt_C += 1
    elif char == "G":
        cnt_G += 1
    elif char == "T":
        cnt_T += 1

print(cnt_A, cnt_C, cnt_G, cnt_T)
