import gzip

transition = 0
transversion = 0
purine = {"A", "G"}
pyrimidine = {"C", "T"}

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:

        if line.startswith("#"):
            continue

        """
        if line.startswith("#"):
            header = line.split("\t")
            REF_idx = header.index("REF")  # 5
            continue
        
        a = line.split("\t")
        if a[3] == "C" and a[4] == "T":
            transition += 1
        elif a[3] == "C" and a[4] == "A":
            transversion += 1
        
        """

        row = line.split("\t")
        ref = row[3]
        alt = row[4]

        if ref in purine and alt in purine:
            transition += 1
        elif ref in pyrimidine and alt in pyrimidine:
            transition += 1
        elif ref in purine and alt in pyrimidine:
            transversion += 1
        elif ref in pyrimidine and alt in purine:
            transversion += 1

print(round(transition / transversion, 4))
