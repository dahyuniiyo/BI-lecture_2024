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
    

