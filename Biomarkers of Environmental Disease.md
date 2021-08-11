# 주제: PubMed을 이용한 환경성 질환의 biomarker 탐색
본 과제에서 NCBI 산하의 데이터베이스인 PubMed의 논문을 이용하여 환경성 질환에 대한 biomarker가 무엇이 있는지 알아보았다.

## 목차
[1. 목적](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#1-%EB%AA%A9%EC%A0%81)

[2. 과정에 대한 Flowchart ](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#2-%EA%B3%BC%EC%A0%95%EC%97%90-%EB%8C%80%ED%95%9C-flowchart)

[3. Progress](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#3-progress)

[3.1 ICD의 질병을 분류](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#31-icd%EC%9D%98-%EC%A7%88%EB%B3%91%EC%9D%84-%EB%B6%84%EB%A5%98)

[3.2 PubMed에서 질병별 Title, Abstract, DOI 추출](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#32-pubmed%EC%97%90%EC%84%9C-%EC%A7%88%EB%B3%91%EB%B3%84-title-abstract-doi-%EC%B6%94%EC%B6%9C)

[3.3 NCBI에 있는 human gene database로부터 총 gene의 개수 파악](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#33-ncbi%EC%97%90-%EC%9E%88%EB%8A%94-human-gene-database%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%B4%9D-gene%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%95%85) 

[3.4 Gene의 symbol과 alias를 PubMed 논문에서 찾기](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#34-gene%EC%9D%98-symbol%EA%B3%BC-alias%EB%A5%BC-pubmed-%EB%85%BC%EB%AC%B8%EC%97%90%EC%84%9C-%EC%B0%BE%EA%B8%B0)

[3.5 Gene과 Disease를 데이터프레임으로 작성](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#35-gene%EA%B3%BC-disease%EB%A5%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84%EC%9C%BC%EB%A1%9C-%EC%9E%91%EC%84%B1)

[3.6 결과해석](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#36-%EA%B2%B0%EA%B3%BC%ED%95%B4%EC%84%9D)

[4. 주요 질환군의 결과 분석](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#4-%EC%A3%BC%EC%9A%94-%EC%A7%88%ED%99%98%EA%B5%B0%EC%9D%98-%EA%B2%B0%EA%B3%BC-%EB%B6%84%EC%84%9D)

[5. 문제점](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#5-%EB%AC%B8%EC%A0%9C%EC%A0%90)

## 1. 목적
본 연구의 목적은 환경성 질환군의 genetic biomarker를 찾고, 데이터베이스를 구축하는 것이다.

환경성 질환은 환경보건법 제2조 제 2호[1]에 따라 환경유해인자와 상관성이 있다고 인정되는 질환 중 감염질환이 아닌 것을 이야기한다. 환경성 질환은 총 6가지의 질환군으로 분류된다. 그 중에서 세 가지 질환군인 알레르기 질환군, 신경계 질환군, 호흡계 질환군을 대상으로 연구를 진행하였다.

더불어 질환군별로 **핵심 질환**을 선정하여
- 알레르기 / 호흡계 질환군: 천식(Asthma), 폐섬유화(Pulmonary Fibrosis)
- 신경계 질환군: 자폐증(Autism Spectrum Disorder), 백질뇌증(Progressive Multifocal Leukoencephalopathy, PML), ADHD(Attention Deficit Hyperactivity Disorder)

탐색할 질환 목록에 포함되도록 했다.

선행된 연구 중에서 genetic biomarker과 disease가 키워드로 포함된 논문을 PubMed에서 찾아, 등장하는 gene과 disease 이름을 파악하여 상관성이 높은 것을 찾는 것이 목표이다.

## 2. 과정에 대한 Flowchart
![프레젠테이션1 (1)](https://user-images.githubusercontent.com/88135502/127962840-e6dca16f-cb88-4828-ac83-bca73fa456bb.jpg)


## 3. Progress

### 3.1 ICD의 질병을 분류
[ICD(International Statistical Classification of Diseases and Related Health Problems)](https://www.who.int/standards/classifications/classification-of-diseases) 는 세계보건기구(WHO)에서 만든, 질병과 증후군에 대한 국제 표준이다. 본 연구에서 사용한 ICD-11는 ICD의 11번째 개정안으로, 2019년 5월에 채택되었고, 2022년 1월 1일부터 효력을 가진다. 

[ICD-11 질병분류](https://icd.who.int/browse11/l-m/en)

우선 ICD-11에서 알레르기 질환군, 신경계 질환군, 호흡계 질환군이 ICD에서 어떤 명칭으로 되어 있는지 살펴보았다. 

- 알레르기 질환군: 04 Diseases of the immune system  / 4A80 - 4A8Z Allergic or hypersensitivity conditions 
- 신경계 질환: 08 Diseases of the nervous system
- 호흡계 질환: 12 Diseases of the respiratory system 

이때, 앞서 제시한 **핵심 질환** 중 천식, 폐섬유화, 자폐증, 백질뇌증은 위에 제시된 항목 내에 존재하지만, ADHD는 06 Mental, behavioural or neurodevelopmental disorders 라는 독립된 챕터에 구분되어 있었다. ADHD는 6A05 - 6A05.Z 항목에 있다. 그렇기 때문에 ADHD만 따로 구분하여 연구과정을 진행하였다. 

ICD-11에서 사용한 전체 질병의 목록은 다음과 같다.

[allrdisease_8-5-2021.txt](https://github.com/Deserav/Environmental-Disease/files/6936430/allrdisease_8-5-2021.txt)

[nervdisease_8-5-2021.txt](https://github.com/Deserav/Environmental-Disease/files/6936431/nervdisease_8-5-2021.txt)

[respdisease_8-5-2021.txt](https://github.com/Deserav/Environmental-Disease/files/6936432/respdisease_8-5-2021.txt)

[ADHD_8-5-2021.txt](https://github.com/Deserav/Environmental-Disease/files/6936437/ADHD_8-5-2021.txt)

이 목록은 위 ICD-11 사이트에서 텍스트를 복사한 것이다. 여기에 동일한 질병이 다른 분류에 속해있는 경우도 있어서, 그런 중복을 제거하고 과정을 진행하였다. 

이렇게 ICD-11에 존재하는 질환군 내의 모든 질병을 파악한다. 그리고 각각의 질병마다 biomarker가 있는지 알아보기 위해, PubMed에서 **"질병명[Title/Abstract]" AND "biomarker[Title/Abstract]"** 를 키워드로 검색했을 때 등장하는 논문의 수를 알아보았다. 그 결과는 다음과 같다.

|         |알레르기 질환군| 신경계 질환군| 호흡계 질환군| ADHD | 계 |
|---------|-------------|------------|-----------|------------|----|
|총 질환 개수|221|2,181|667| 6 | 3075 |
|총 질환 개수(중복 제거)|201|2,108|655|6| 2970|
|논문이 존재하는 질환의 개수|**30**|**256**|**93**|**1**|**380**|
|논문의 수|2,226|9,589|6,810|205|18,830|
|Gene이름이 등장하는 논문의 수*|1,537|7,694|5,103|125|14,459|

**총 18,830편의 논문**

\* 섹션 3.4에 결과 첨부 및 설명

위 결과에서 논문이 존재하는 질환만을 따로 모아 txt 파일로 정리하였고, 아래에 첨부하였다.

[allrDB_shredded_list_refined.txt](https://github.com/Deserav/Environmental-Disease/files/6943220/allrDB_shredded_list_refined.txt) **총 30개의 질환**

[nervDB_shredded_list_refined.txt](https://github.com/Deserav/Environmental-Disease/files/6943221/nervDB_shredded_list_refined.txt) **총 256개의 질환**

[respDB_shredded_list_refined.txt](https://github.com/Deserav/Environmental-Disease/files/6943222/respDB_shredded_list_refined.txt) **총 93개의 질환**

[ADHD_shredded_list_refined.txt](https://github.com/Deserav/Environmental-Disease/files/6943385/ADHD_shredded_list_refined.txt) **총 1개의 질환**

이후에 편의를 위해 '논문이 존재하는 질환'을 간략히 파일명과 같이 shredded list로 부르기로 한다.

반면, 논문이 존재하는 질환을 대상으로, 각 질환이 몇 개의 논문을 가지고 있는지 다음과 같이 정리하였다.

[allrDB_number_of_papers.txt](https://github.com/Deserav/Environmental-Disease/files/6943230/allrDB_number_of_papers.txt)

[nervDB_number_of_papers.txt](https://github.com/Deserav/Environmental-Disease/files/6943231/nervDB_number_of_papers.txt)

[respDB_number_of_papers.txt](https://github.com/Deserav/Environmental-Disease/files/6943232/respDB_number_of_papers.txt)

[ADHD_number_of_papers.txt](https://github.com/Deserav/Environmental-Disease/files/6943277/ADHD_number_of_papers.txt)


이로써 ICD-11에 분류되어 있는 알레르기 질환, 신경계 질환, 호흡계 질환 중에 PubMed 데이터베이스에 존재하는 질병의 목록, 논문의 수를 확보하게 되었다.

### 3.2 PubMed에서 질병별 Title, Abstract, DOI 추출
Python의 Biopython 모듈로부터 Entrez와 Medline 모듈을 사용하여, 검색 키워드로부터 등장하는 논문들의 Title, Abstract, DOI를 전부 하나의 txt 파일로 정리하였다. 3.1 단계에 첨부한 각각의 txt 파일에 등장한 질병들을 모듈의 input으로 하여 다음의 과정을 진행하였다.

- ICD-11에서 찾은 개별적인 질명에 biomarker라는 키워드와 결합하여 **"질병명"[Title/Abstract] AND "biomarker"[Title/Abstract]** 로 검색하였다. 질병명을 정확히 찾기 위해 '질병명'과 'biomarker'에 큰따옴표 처리를 한다.
- 각 질병마다 검색 결과로 나타나는 논문들의 Title, Abstract, DOI를 txt 파일로 정리하였다. 
 
이런 식으로 Python을 이용하여 알레르기 질환 30개, 신경계 질환 256개, 호흡계 질환 93개, ADHD 질환 1에 txt 파일을 만들어, 논문의 Title, Abstract, DOI를 저장하였다.


### 3.3 NCBI에 있는 human gene database로부터 총 gene의 개수 파악
온라인 [오픈 소스 biomarker 데이터베이스](https://markerdb.ca/) 가 있기는 하지만, 등장하는 질병의 수와 gene의 수가 매우 한정적이었다. 그래서 human gene을 전수조사 하는 과정을 진행하였다. 

NCBI에서 제공한 raw data에 대한 파일은 다음과 같다.

[gene_result.txt](https://github.com/Deserav/Environmental-Disease/files/6920740/gene_result.txt)

이 데이터를 보면 각 gene 마다 symbol과 alias가 있다. 각 symbol과 alias를 하나의 문자열로 생각했을 때, 이 문자열이 3.2 단계에서 찾은 논문에 과연 존재하는지 알아보기로 했다. 그러기 위해서는 이 데이터에서 유의미한 문자열만 골라내야 했다. 다음과 같은 과정을 통해 필요한 문자열만 골라냈다.

1. NCBI에 등장하는 63,750개의 (pseudogene, tRNA gene 등을 포함) gene의 symbol과 alias를 전부 추출하였다.
2. Gene과 aliase에 중복인 것을 제거했을 때, 127,994개의 서로 다른 문자열이 생성되었다.
3. 한 글자 문자열 8개, nan을 제거하면 127,994 - 9 = 127,985개의 문자열이 남는다.
4. 두 글자 문자열 422개, 세 글자 문자열 4,418개 중에서 자주 사용하는 단어와 철자가 같은 것을 제거했다.
 - II, IN, KO, ME, TO, UP, AM, DO, IV, CO, IF, GO, OK, ID, OF, AN, NA, AS: 18 종류
 - SOS, BUG, CAM, ATP, MAX, OUT, FAN, VIP, CAR, LED, APE, RED, NOT, DUO, SHE, ICE, GAS, ENG, FAD, GAP, SET, AIM, SIT, PEN, WAS, PIN, CAN, ZIP, AIR, ARM, AID, GET, TIP, FOG, APP, HOT, BAR, SON, SEA, NOV, HUB, ACT, FOR, CAR, OUT, NOT, AIM, CAN, SEA, PDF, VIA, bet, FAN, HOT, PEN, LAB, ECM, not: 49 종류

최종적으로 127,985 - ( 18 + 49 ) = 127,918의 문자열을 가지고 다음 단계를 진행하였다. 이때 사용한 gene과 alias의 목록은 다음과 같이 첨부했다.

[final_genelist.txt](https://github.com/Deserav/Environmental-Disease/files/6943375/final_genelist.txt)


### 3.4 Gene의 symbol과 alias를 PubMed 논문에서 찾기
전 단계에서 선정한 127,918개의 문자열과 18,830 논문의 Abstract와 비교하였다. 이렇게 문자열 비교를 통해 논문마다 등장하는 gene의 종류, 빈도를 계산하였다. 그리고 최종적으로 질환 하나에 등장하는 gene의 종류, 개수, 빈도를 계산하였다. 이 결과를 zip로 첨부하였다. 이 파일의 구성은 다음과 같다.
- Shredded list 에 등장하는 질환에 대해 개별적인 파일을 만들고, 파일명을 "질병명 + output"으로 칭한다.
- 챕어 3.2에서 다운로드 받은 논문과 챕터 3.3의 gene 목록을 비교. Gene이 등장하는 논문들만 output 파일에 들어간다. 즉, 논문에 gene의 이름이 없으면 output 파일에 들어가지 않는다.
- 하나의 파일에 있는 정보는 다음과 같다.
  - gene이 존재하는 논문과, gene의 이름
  - gene의 이름
  - gene의 등장 빈도
- 파일의 말미에는 다음의 정보가 있다.
  - 지금까지 발견한 gene의 수
  - 지금까지 발견한 gene의 종류
  - 지금까지 발견한 gene의 빈도


데이터의 양이 많기 때문에, 아래는 중요한 결과를 요약한 것이다. 다음은 질환별 논문에 등장하는 gene과 alias의 종류와 빈도에 대한 결과이다.

[allrDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6946517/allrDB_count.txt)

[nervDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6946521/nervDB_count.txt)

[respDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6946524/respDB_count.txt)

[ADHD_count.txt](https://github.com/Deserav/Environmental-Disease/files/6928796/ADHD_count.txt)


아래는 질환군별로 등장하는 gene과 alias가 표시되어 있다.

[allrDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6946539/allrDB_gene_set.txt)

[nervDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6946536/nervDB_gene_set.txt)

[respDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6946534/respDB_gene_set.txt)

[ADHD_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6928808/ADHD_gene_set.txt)


그 결과, 질환군별로 나타나는 gene + alias 의 개수는 알레르기 질환군 869개, 신경계 질환군 2,223개, 호흡계 질환군 1,831 개, ADHD가 120개였다.

마지막으로, 질환군별로, 각 질환마다 gene 이름이 존재하는 논문의 수에 대한 데이터이다. 마지막 줄에는 질환군에서 gene 이름에 포함된 논문의 수가 쓰여 있다.

[allrDB_number_of_papers_thathave_gene.txt](https://github.com/Deserav/Environmental-Disease/files/6948694/allrDB_number_of_papers_thathave_gene.txt)

[nervDB_number_of_papers_thathave_gene.txt](https://github.com/Deserav/Environmental-Disease/files/6948695/nervDB_number_of_papers_thathave_gene.txt)

[respDB_number_of_papers_thathave_gene.txt](https://github.com/Deserav/Environmental-Disease/files/6948696/respDB_number_of_papers_thathave_gene.txt)

[ADHD_number_of_papers_thathave_gene.txt](https://github.com/Deserav/Environmental-Disease/files/6948697/ADHD_number_of_papers_thathave_gene.txt)

챕터 3.1 표에 표시한 것처럼 gene이 등장하는 논문의 수는 알레르기가 1,537개, 신경계가 7,694개, 호흡계가 5,103개, ADHD가 1,25개이다.

### 3.5 Gene과 Disease를 데이터프레임으로 작성
챕터 3.4에 있는 count 파일을 바탕으로, 질병과 gene에 대한 데이터프레임으로 정리하였다. Column name의 뜻은 다음과 같다
- Disease: 질환 이름
- Category: Allergy - 알레르기 질환군, Nerve - 신경계 지환군, Respire - 호흡계 질환군, ADHD - ADHD 질환
- Match: 일치한 문자열.
- Original_gene: Match의 결과가 symbol일 수도 있고, alias일 수도 있다. Alias와 일치한 경우 symbol의 이름을 보여준다.

[gene_disease_original.txt](https://github.com/Deserav/Environmental-Disease/files/6948958/gene_disease_original.txt)

여기서 우리는 Original_gene을 genetic biomarker로 생각하고 결과를 분석하려 한다.

### 3.6 결과해석
질병과 biomarker의 상관성은, 기준을 질병으로 볼때와 biomarker로 볼때가 다르기 때문에 따로 결과를 명시하였다.

#### 3.6.1 Disease - Biomarker Link

각 질환별로 biomarker의 종류는 다음과 같다
[types_of_biomarker_per_disease.txt](https://github.com/Deserav/Environmental-Disease/files/6949169/types_of_biomarker_per_disease.txt)

각 질환의 biomarker의 수는 다음과 같다.
[number_of_biomarker_per_disease.txt](https://github.com/Deserav/Environmental-Disease/files/6950667/number_of_biomarker_per_disease.txt)

가장 아래줄에 지금까지 나온 biomarker의 수가 나타있는데, 총 **16,821개** 이다. 이 수치는 중복된 질병을 제외한 수치이다.

질환군별로 정리했을 대는  다음과 같다.
1. 알레르기 질환군: **총 1933개**
  - 종류: [allrDB_types_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950514/allrDB_types_of_biomarkers.txt)

  - 개수: [allrDB_number_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950525/allrDB_number_of_biomarkers.txt)

2. 신경계 질환군: **총 9533개**
  - 종류: [nervDB_types_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950516/nervDB_types_of_biomarkers.txt)
  
  - 개수: [nervDB_number_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950520/nervDB_number_of_biomarkers.txt)

3. 호흡계 질환군: **총 6634개**
  - 종류: [respDB_types_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950521/respDB_types_of_biomarkers.txt)

  - 개수: [respDB_number_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950522/respDB_number_of_biomarkers.txt)

4. ADHD 질환군: **총 175개**
  - 종류: [ADHD_types_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950523/ADHD_types_of_biomarkers.txt)
  
  - 개수: [ADHD_number_of_biomarkers.txt](https://github.com/Deserav/Environmental-Disease/files/6950524/ADHD_number_of_biomarkers.txt)

이 네 항목의 biomarker 수를 모두 합하면 18,275개로, 앞서 구한 16,821보다 1,454개가 많다. 그 이유는 ICD-11 분류상 알레르기 질환군과 호흡계 질환 군 중 비염(Rhinitis)과 천식(Asthma) 관련 질병이 중복되기 때문이다. 중복되는 질병명은 다음과 같다.

- Allergic rhinitis: 188
- Non-allergic rhinitis:	24
- Chronic rhinosinusitis:	143
- Nasal polyp:	33
- Asthma:	905
- Allergic asthma:	134
- Non-allergic asthma:	18

총 1,454개의 중복

#### 3.6.2 Biomarker - Disease Link
바이오마커를 기준으로 삼은 경우, 하나의 바이오마커에 여러 개의 disease가 나타나는 경우가 있다. 이런 biomarker의 수를 찾기 위해 Venn Diagram으로 정리하였다.
![venn_diagram](https://user-images.githubusercontent.com/88135502/128726696-6c400a69-5947-4f13-9733-5b29c4cd611a.png)


## 4. 핵심 질환의 결과 분석

### 4.1 핵심 질환 biomarker 데이터
PubMed 논문에서 찾은 핵심 질환의 biomarker의 종류와 수는 다음과 같다

1. 천식(Asthma) (905개) : [Biomarkers_Asthma.txt](https://github.com/Deserav/Environmental-Disease/files/6949176/Biomarkers_Asthma.txt)
  - Asthma: 905개
  - Allergic Asthma: 134개
  - Non-Allergic Asthma: 18개
2. 폐섬유화(Idiopathic Pulmonary Fibrosis) (330개) : [Biomarkers_Idiopathic_Pulmonary_Fibrosis.txt](https://github.com/Deserav/Environmental-Disease/files/6949182/Biomarkers_Idiopathic_Pulmonary_Fibrosis.txt)
3. 자폐증(Autisum Spectrum Disorder) (345개) : [Biomarkers_Autism_Spectrum_Disorder.txt](https://github.com/Deserav/Environmental-Disease/files/6949183/Biomarkers_Autism_Spectrum_Disorder.txt)
4. 백질뇌증(Progressive Multifocal Leukoencephalopathy) (31개) : [Biomarkers_Progressive_Multifocal_Leukoencephalopathy.txt](https://github.com/Deserav/Environmental-Disease/files/6949184/Biomarkers_Progressive_Multifocal_Leukoencephalopathy.txt)
5. ADHD (Attention Deficit Hyperactivity Disorder) (175개) : [Biomarkers_ADHD.txt](https://github.com/Deserav/Environmental-Disease/files/6949187/Biomarkers_ADHD.txt)

반면 MarkerDB에서 제공한 데이터로부터, 핵실 질환의 biomarker은 다음과 같다.

1. 천식 (Asthma) : 2개 (NOTCH4, BRCA2)
2. 폐섬유화 (Idiopathic Pulmonary Fibrosis) : 0개
3. 자폐증 (Autism Spectrum Disorder) : 1개 (MACROD2)
4. 백질뇌증 (Progressive Multifocal Leukocephalopathy) : 0개
5. ADHD (Attention Deficit Hyperactivity Disorder) : 0개

이 데이터베이스에서 제공한 biomarker 중에서 핵심 질환에 관련된 biomarker가 3개뿐이었다. NOTCH4, BRCA2, MACROD2이 그것인데, 챕터 3.4의 분석 과정에서 등장하지 않았던 gene들이었다.

[Asthma_output.txt](https://github.com/Deserav/Environmental-Disease/files/6958690/Asthma_output.txt)

[Autism spectrum disorder_output.txt](https://github.com/Deserav/Environmental-Disease/files/6958688/Autism.spectrum.disorder_output.txt)

그 이유는 검색 시 "biomarker"라는 키워드가 추가되면서, 이 gene들이 검색 결과에서 누락되었기 때문이다.

```
search1 = '"Autism spectrum disorder"[Title/Abstract] AND "biomarker"[Title/Abstract] AND "MACROD2"[Title/Abstract]'
handle1 = Entrez.esearch(db = "pubmed", term = search1) # the process to find how many papers in a single search keyword
record1 = Entrez.read(handle1)
handle1.close()
count1 = int(record1["Count"])

print(count1)
```
위와 같이 검색하는 경우 결과의 개수가 0이다.

### 4.2 유사한 질병과 같이 분석
백질뇌증과 폐섬유화의 경우, 비슷한 증상을 가진 질병과 연관되어 있는 경우가 있어, 이에 대한 분석이 필요했다.
Output file을 통해, 다음의 질병이 연관이 있다는 것을 알 수 있었다.

1. 폐섬유증(Idiopathic pulmonary fibrosis, IPF), 만성폐쇄성폐질환(Chronic Obstructive Pulmonary Disease, COPD), 낭포성 섬유증(Cystic fibrosis, CF)
2. 백질뇌증(Progressive multifocal leukoencephalopathy, PML), 다발성 경화증(Multiple sceloris)

마찬가지로 이 질병들도 MarkerDB에서 biomarker가 존재하는지 알아보았고, 그 결과는 다음과 같았다. 

1. 다발성 경화증 (Multiple sclerosis, MS) : 3개 (IL2RA, TNFRSF1A, IL7R)
2. 만성폐쇄성폐질환 (Chronic Obstructive Pulmonary Disease, COPD): 0개
3. 낭포성 섬유증 (Cystic fibrosis, CF) : 1개 (CFTR)

여기서 찾은 gene은 IL2RA, TNFRSF1A, IL7R, CFTR 네 종류였다. 데이터프레임에서 이 gene들에 나타는 질병은 다음과 같다.

1. IL2RA: Idiopathic pulmonary fibrosis, Pneumonia, Chronic bronchiolitis, Allergic asthma, Asthma, Chronic obstructive pulmonary disease, Coma, Myelopathy, Status elipticus, Multiple sclerosis
2. TNFRSF1A: Chronic obstructive pulmonary disease, Concussion, Coma
3. IL7R: Multiple sclerosis
4. CFTR: Cystic fibrosis, Bronchiectasis, Asthma

데이터프레임을 바탕으로 유사한 질병끼리 모아 Venn Diagram으로 표현하였다.

![Figure_1](https://user-images.githubusercontent.com/88135502/128814868-dca4240d-275a-4dca-bbc8-5427765202f2.png)

![Figure_2](https://user-images.githubusercontent.com/88135502/128814882-66ceefcf-9424-4827-8f60-5aeefcf2e69f.png)

두 번째 그림에서 눈여겨 볼 것은, PML의 biomarker 집합은 MS의 부분집합이라는 것이다. PML의 biomarker 31종류 전부 MS 내에 포함이 되어 있었다.

![resp](https://user-images.githubusercontent.com/88135502/128962914-f678051c-434c-4186-9631-037ad9dfda8c.jpg)

![nerv](https://user-images.githubusercontent.com/88135502/128962926-333bbee5-ba00-4eaf-bf03-586cb8427a03.jpg)

![brain](https://user-images.githubusercontent.com/88135502/128962932-4d945985-3c2d-4a09-9ee9-39ed82c0c0c1.jpg)


## 5. 문제점
최종적으로 genetic biomarker에 대한 데이터베이스를 마련하기 위해 해결해야 할 문제들은 다음과 같다.
- 질병명의 약자와 gene symbol이 같은 경우: 예를 들어 CAP라는 문자열은 BRD4 gene의 alias 중 하나이지만, community acquired pneumonia의 약자이기도 하다. 문자열로 비교할 때, 우리가 찾은 문자열이 논문 내에서 gene으로 쓰이건지, 다른 의미로 쓰인 건지 파악하기 어렵다.
- 알려진 genetic biomarker에 대한 데이터 부족: 많은 biomarker 데이터베이스는 protein, metabolite을 기준으로 하고 있다. Genetic biomarker이 나와있는 데이터베이스가 필요하다. RFP에서 사용할 데이터베이스로 ENCODE, IHEC, SRA, GEO, Charles River Biomarker DB, ResMarkerDB, GOBIOM, IDBD를 제시했지만, 다음과 같은 이유로 부적합하다고 판단했다.
  - IDBD: 감염성 질환에 대한 biomarker가 나와있다. 환경성 질환은 비감염성을 전제로 하고 있기 때문에 부적합
  - GOBIOM: 라이선스 필요
  - ResMarkerDB: Immunoglobulin biomarker를 주로 하고, cancer에 대한 데이터가 주력

나머지 데이터베이스에 대해서 좀 더 조사가 필요하다.
- Biomarker와 disease의 상관성을 입증할 방법 필요: 어떠한 통계적인 방법으로 상관성을 입증할 수 있는지 피드백이 필요하다.
- Gene의 이름은 고정되어 있지만, alias가 같지만 gene 이름이 다른 경우가 있다. 예를 들어 CD14라는 문자열은 CD14 gene 일수도 있고, NDUFA2의 alias일 가능성도 있다.
- 논문 내용에 biomarker라는 단어가 없을 때, 우리가 원하는 gene이 있어도 찾을 수 없다는 문제가 있다. 챕터 4에서 보았듯이, 검색 키워드에 "biomarker"를 추가함으로써, 프로그램이 NOTCH4, BRCA2, MACROD2를 찾아내지 못하는 일이 발생하였다. 
