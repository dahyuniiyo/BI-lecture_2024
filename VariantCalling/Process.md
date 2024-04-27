# Variant Calling   


### 실습경로 ~/etc/bwa

* **BWA설치**
    * bwa github 을 검색
    * bwa github 페이지에 들어간다
    * Getting started에 내용대로 커맨드라인 수행
    * make --> ./bwa 수행 
    * sudo ln -s ~/etc/bwa/bwa/bwa
    * which bwa 
    
***

### 실습경로 ~/etc/reference

* **Download reference genome**
    * ucsc genome browser 검색   
    * Downloads 탭 클릭
    * wget + 링크
    


* **reference file에 대해 index 만들기**  
    * ~/etc/reference$ bwa index chr1.fa.gz   

***

### 실습경로 ~/Analysis/sample

* **FASTQ 파일 다운로드**  

    * 정방향 리드와 역방향 리드에 대한 sample1, sample2 두개의 파일이 필요하다.   
    * wget을 사용하여 다음 두 링크를 다운받는다.   

        * https://github.com/KennethJHan/GenomeAnalysisTutorial/raw/main/data/sample_1.fastq.gz   

        * https://github.com/KennethJHan/GenomeAnalysisTutorial/raw/main/data/sample_2.fastq.gz   


* **Mapping to reference**

    * bwa mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ~/etc/reference/chr21.fa.gz sample_1.fastq.gz sample_2.fastq.gz > sample.sam

* **SAM to BAM**
    * samtools view -Sb sample.sam > sample.chr1.mapped.bam   

* **BAM sorting**   
    *  samtools sort sample.chr1.mapped.bam -o sample.chr1.sorted.bam   

* **BAM indexing**
    * samtools index sample.chr1.sorted.bam  

* **BAM 살펴보기**  
    * 전체 내용 확인 : samtools view -h sample.chr21.sorted.bam 
    * 헤더 확인 : samtools view -H sample.chr21.sorted.bam  
    * 리드를 눈으로 확인하는 법 : samtools tview sample.chr21.sorted.bam  --> /키 입력 후 position을 입력한다
    
### 실습경로 ~/etc/picard

* **picard 설치**
    * wget https://github.com/broadinstitute/picard/releases/download/3.1.1/picard.jar
    * 잘 다운받아졌는지 확인 : ls -lh ~/etc/picard/picard.jar
* **java 설치/확인**
    * sudo apt update
    * sudo apt search openjdk-17-jdk
    * sudo apt install openjdk-17-jdk
    * which java
    * java -version
* **picard 구동**
    * java -jar picard.jar 
    * picard 의 여러 기능 중 MarkDuplicates 가 있는지
    확인
    * java -jar picard.jar MarkDuplicates 로 
    picard의 Markduplicates 를 수행하여
    수행에 필요한 input, output 등의
    인자들을 확인

### 실습경로 ~/Analysis/sample

* **Markduplicate**
    * java -jar ~/etc/picard/picard.jar MarkDuplicates -I sample.chr21.sorted.bam -O sample.markdup.bam -M sample.metrics.txt
    * 확인 :  ll -tr

* **Markduplicate 확인**
    * Explain SAM Flags 
    * 여러 flag 중 원하는 유형 선택 (10번째 flag면 2^10)
    * samtools option 중에 -f 옵션은 해당 flag를 포함한 read 만 가져오게 해준다
    * -F 는 해당 flag를 제외한 read를 가져온다
    * samtools view -f1024 sample.markdup.bam | wc -l
    * samtools view -F1024 sample.markdup.bam | wc -l
    
### 실습경로 ~/etc/gatk
* **GATK다운로드**
    * wget https://github.com/broadinstitute/gatk/releases/download/4.5.0.0/gatk-4.5.0.0.zip
    * unzip gatk-4.5.0.0.zip
    * cd gatk-4.5.0.0/
    * java -jar gatk-package-4.5.0.0-local.jar

* **reference 준비**
    * 경로 ~/etc/reference
    * gunzip chr21.fa.gz
    * sudo apt install tabix
    * bgzip chr21.fa
    * samtools faidx chr21.fa.gz
    *  java -jar ~/etc/picard/picard.jar CreateSequenceDictionary -R chr21.fa.gz

### 실습경로 ~/Analysis/sample

* **variant calling**
    * 목적 : markdup.bam --> g.vcf.gz --> vcf.gz
    * **Halotype Caller 사용 : BAM --> GVCF**
        * samtools index sample.markdup.bam
        
        * java -jar ~/etc/gatk/gatk-4.5.0.0/gatk-package-4.5.0.0-local.jar HaplotypeCaller -I sample.markdup.bam -O sample.g.vcf.gz -R ~/etc/reference/chr21.fa.gz -ERC GVCF

        * 확인 : zless -S sample.g.vcf.gz / zcat sample.g.vcf.gz |head -100
    
    * **GenotypeGVCFs 사용 : GVCF --> VCF**
        * java -jar ~/etc/gatk/gatk-4.5.0.0/gatk-package-4.5.0.0-local.jar GenotypeGVCFs -V sample.g.vcf.gz -O sample.vcf.gz -R ~/etc/reference/chr21.fa.gz
        * 확인 : ll -tr

* **snpEff_Annotation**
* snpEff downloads
    * mkdir ~/download
    * wget https://snpeff.blob.core.windows.net/versions/snpEff_latest_core.zip
    * unzip snpEff_latest_core.zip
    * cd ~downloads/snpEff/
    * java -jar snpEff.jar
* snpEff 수행 : annotation
    * annotation을 통해 vcf파일에서 변이에 대한 정보를 확인할 수 있다.
    * java -jar ~/Downloads/snpEff/snpEff.jar -v hg38 sample.vcf.gz > sample.ann.vcf
* 확인
    * zgrep intron_variant sample.ann.vcf | wc -l
    * zgrep intergenic_region sample.ann.vcf | wc -l
    * zgrep stop_gained sample.ann.vcf | wc -l
