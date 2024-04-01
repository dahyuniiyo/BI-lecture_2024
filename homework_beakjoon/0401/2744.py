a = input()
result = ""

for i in a:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()

print(result)
