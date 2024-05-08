import gzip

gt_count = dict()  # 딕셔너리를 사용하면 key를 모르는 상태에서 세어도 키값까지 알려줌

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        row = line.strip().split("\t")  # 리스트로 가져와짐
        # print(row[-1])
        gt = row[-1].split(":")[0].replace("|", "/")  # 파이프를 슬래시로 바꿈
        # print(gt)
        # _ = input()  # 한줄씩 과정을 볼 수 있음
        if gt not in gt_count:
            gt_count[gt] = 0

        gt_count[gt] += 1

print(gt_count)
