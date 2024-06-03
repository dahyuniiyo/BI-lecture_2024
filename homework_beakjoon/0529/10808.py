a = dict(str(input()))

Alphabet = "abcdefghijklmnopqrstuvwxyz"

cnt = 0

for i in a:
    if i in Alphabet:
        idx = Alphabet.find(i)
        cnt += 1

print(cnt)
print(idx)
