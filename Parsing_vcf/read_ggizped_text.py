with open("test.txt.gz") as handle:
    for line in handle:
        print(line.strip())
