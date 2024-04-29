import gzip

result = 0
with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:

        if line.startswith("#"):
            continue

        a = line.split("\t")

        if float(a[5]) >= 1000:
            result += 1

print(result)
