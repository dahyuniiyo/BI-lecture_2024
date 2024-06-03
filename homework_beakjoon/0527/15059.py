f1, f2, f3 = map(int, input().split())
p1, p2, p3 = map(int, input().split())

cnt = 0

for i in range(1, 4):
    f_var = globals()[f"f{i}"]
    p_var = globals()[f"p{i}"]

    if f_var < p_var:
        a = p_var - f_var
    else:
        continue

    cnt += a

print(cnt)
