handle = open("test.txt")
for line in handle:
    # print(line.replace("\n", ""))
    print(line.strip())  # 자동적으로 들어가는 enter제거 방법

handle.close()
