N = input()

for i in range(int(N)):

    if "7" in str(N):
        if int(N) % 7 != 0:
            result = 2
        elif int(N) % 7 == 0:
            result = 3
    else:
        if int(N) % 7 != 0:
            result = 0
        elif int(N) % 7 == 0:
            result = 1

print(result)
