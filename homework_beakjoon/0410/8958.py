data = str(input())

score = 0
count = 0

for char in data:
    if char == "O":
        count += 1
        score += count
    else:
        count = 0

print(score)
