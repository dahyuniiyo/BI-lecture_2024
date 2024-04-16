N = int(input())

for i in range(N):

    R, S = input().split()

    X = int(R)
    data = list(S)

    if data:
        for char in data:
            print(char * X, end="")

    print()
