import gzip

result = 0
with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        # print(line.strip())
        if line.startswith("#"):
            continue  # #으로 시작하는건 제껴버리고 센다는 뜻

        result += 1

    print(result)
