# QUAL이 몇번째인지 모를때 5로 인덱스하지 않고도 찾을 수 있는 방법. 예를들어 실시간으로 QUAL 데이터 정보가 바뀔 때 등

import gzip

result = 0

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:

        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.split("\t")
            qual_idx = header.index("QUAL")  # 5
            continue

        a = line.split("\t")
        if float(a[qual_idx]) >= 1000:
            result += 1

print(result)
