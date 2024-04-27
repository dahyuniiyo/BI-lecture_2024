seq = ""
with open("test_aa.fasta") as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        seq += line.strip()

data = dict()
for aa in seq:
    if aa not in data:
        data[aa] = 0
    data[aa] += 1

print(data)
