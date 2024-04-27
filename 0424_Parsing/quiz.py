result = 0

for i in range(1, 11):
    result += 1

print(result)


seq = ""
with open("test.fasta") as handle:
    for line in handle:
        if line.strartwith(">"):
            continue
        seq += line.strip()


print(len(seq))
print(f'A: {seq.count("A")}')
print(f'C: {seq.count("C")}')
print(f'G: {seq.count("G")}')
print(f'T: {seq.count("T")}')
