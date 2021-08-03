# 주제: PubMed을 이용한 환경성 질환의 biomarker 탐색
본 과제에서 NCBI 산하의 데이터베이스인 PubMed의 논문을 이용하여 환경성 질환에 대한 biomarker가 무엇이 있는지 알아보았다.

## 목차
[1. 목적](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#1-%EB%AA%A9%EC%A0%81)

[2. 과정에 대한 Flowchart ](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#2-%EA%B3%BC%EC%A0%95%EC%97%90-%EB%8C%80%ED%95%9C-flowchart)

[3. Progress](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#3-progress)

[3.1 ICD의 질병을 분류](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#31-icd%EC%9D%98-%EC%A7%88%EB%B3%91%EC%9D%84-%EB%B6%84%EB%A5%98)

[3.2 PubMed에서 질병별 Title, Abstract, DOI 추출](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#32-pubmed%EC%97%90%EC%84%9C-%EC%A7%88%EB%B3%91%EB%B3%84-title-abstract-doi-%EC%B6%94%EC%B6%9C)

[3.3 NCBI에 있는 human gene database로부터 총 gene의 개수 파악](https://github.com/Deserav/Environmental-Disease/blob/main/Biomarkers%20of%20Environmental%20Disease.md#33-ncbi%EC%97%90-%EC%9E%88%EB%8A%94-human-gene-database%EB%A1%9C-%EB%B6%80%ED%84%B0-%EA%B0%81-%EB%85%BC%EB%AC%B8%EB%B3%84-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-gene-%ED%8C%8C%EC%95%85)

[]

## 1. 목적
본 연구의 목적은 환경성 질환군의 genetic biomarker를 찾고, 데이터베이스를 구축하는 것이다.

환경성 질환은 환경보건법 제2조 제 2호[1]에 따라 환경유해인자와 상관성이 있다고 인정되는 질환 중 감염질환이 아닌 것을 이야기한다. 본 보고서에는 6가지 환경성질환군 중에서 RFP에서 요구한
- 알레르기 질환군
- 신경계 질환군
- 호흡계 질환군

위 3가지에 대해서 연구를 진행하였다.

현재까지 선행연구 중에서 genetic biomarker과 disease가 키워드로 포함된 논문을 PubMed에서 찾아, 등장하는 gene과 disease 이름을 파악하여 상관성이 높은 것을 찾는 것이 목표이다.

## 2. 과정에 대한 Flowchart

## 3. Progress

### 3.1 ICD의 질병을 분류
ICD(International Statistical Classification of Diseases and Related Health Problems) [2] 는 세계보건기구(WHO)에서 만든, 질병과 증후군에 대한 국제 표준이다. 본 연구에서 사용한 ICD-11는 ICD의 11번째 개정안으로, 2019년 5월에 채택되었고, 2022년 1월 1일부터 효력을 가진다. 

우리는 ICD-11에서 알레르기 질환군, 신경계 질환군, 호흡계 질환군에 어떤 질환들이 포함되어 있는지 파악하였다. 그리고 각 질병마다 biomarker가 있는지 알아보기 위해, PubMed에서 **(질병명[Title/Abstract]) AND (biomarker[Title/Abstract])** 를 키워드로 검색했을 때 등장하는 논문의 수를 알아보았다. 그 결과는 다음과 같다.

|         |알레르기 질환군| 신경계 질환군| 호흡계 질환군|
|---------|-------------|------------|-----------|
|총 질환 개수|385|2175|667|
|논문이 존재하는 질환의 개수|**149**|**652**|**215**|
|논문의 수|38,458|383,659|180,255|

**총 602,372편의 논문**

위 결과에서 논문이 존재하는 질환만을 따로 모아 txt 파일로 정리하였고, 아래에 첨부하였다.

[allrDB_shredded_list.txt](https://github.com/Deserav/Environmental-Disease/files/6914676/allrDB_shredded_list.txt)

[nervDB_shredded_list.txt](https://github.com/Deserav/Environmental-Disease/files/6914677/nervDB_shredded_list.txt)

[respDB_shredded_list.txt](https://github.com/Deserav/Environmental-Disease/files/6914678/respDB_shredded_list.txt)

반면, 개별 질병에 대한 논문의 수를 다음과 같이 정리하였다.

[allr_DB.xlsx](https://github.com/Deserav/Environmental-Disease/files/6915474/allr_DB.xlsx)

[nerv_DB.xlsx](https://github.com/Deserav/Environmental-Disease/files/6915475/nerv_DB.xlsx)

[resp_DB.xlsx](https://github.com/Deserav/Environmental-Disease/files/6915473/resp_DB.xlsx)

이로써 ICD-11에 분류되어 있는 알레르기 질환, 신경계 질환, 호흡계 질환 중에 PubMed 데이터베이스에 존재하는 질병의 목록, 논문의 수를 확보하게 되었다.

### 3.2 PubMed에서 질병별 Title, Abstract, DOI 추출
Python의 Biopython 모듈로부터 Entrez와 Medline 모듈을 사용하여, 검색 키워드로부터 등장하는 논문들의 Title, Abstract, DOI를 전부 하나의 txt 파일로 정리하였다. 3.1의 각 txt 파일에 등장한 질병들을 모듈의 input으로 하여 다음의 과정을 진행하였다.

- ICD-11에서 찾은 개별적인 질명에 biomarker라는 키워드와 결합하여 **(질병명[Title/Abstract]) AND (biomarker[Title/Abstract])** 로 검색하였다. 
- 각 질병마다 검색 결과로 나타나는 논문들의 Title, Abstract, DOI를 txt 파일로 정리하였다. 
 
이런 식으로 Python을 이용하여 알레르기 질환 149개, 신경계 질환 652개, 호흡계 질환 215개에 txt 파일을 만들어, 논문의 Title, Abstract, DOI를 저장하였다.


### 3.3 NCBI에 있는 human gene database로부터 총 gene의 개수 파악
온라인 오픈 소스 biomarker 데이터베이스가 있기는 하지만, 등장하는 질병의 수와 gene의 수가 매우 한정적이었다. 때문에 우리는 human gene을 전수조사 하는 과정이 필요하다고 느꼈다. 

NCBI에서 제공한 raw data에 대한 파일은 다음과 같다

[gene_result.txt](https://github.com/Deserav/Environmental-Disease/files/6920740/gene_result.txt)

이 데이터를 보면 각 gene 마다 symbol과 alias가 있다. 각 symbol과 alias를 하나의 문자열로 생각했을 때, 이 문자열이 3.2 단계에서 찾은 논문에 과연 존재하는지 알아보기로 했다. 그러기 위해서는 이 데이터에서 유의미한 문자열만 골라내야 했다. 다음과 같은 과정을 통해 필요한 문자열만 골라냈다.

1. NCBI에 등장하는 63,750개의 (pseudogene, tRNA gene 등을 포함) gene의 symbol과 alias를 전부 추출하였다.
2. Gene과 aliase에 중복인 것을 제거했을 때, 127,994개의 서로 다른 문자열이 생성되었다.
3. 한 글자 문자열 8개, nan을 제거하면 127,994 - 9 = 127,985개의 문자열이 남는다.
4. 두 글자 문자열 422개, 세 글자 문자열 4,418개 중에서 자주 사용하는 단어와 철자가 같은 것을 제거했다.
 - II, IN, KO, ME, TO, UP, AM, DO, IV, CO, IF, GO, OK, ID, OF, AN, NA, AS: 18종류
 - SOS, BUG, CAM, ATP, MAX, OUT, FAN, VIP, CAR, LED, APE, RED, NOT, DUO, SHE, ICE, GAS, ENG, FAD, GAP, SET, AIM, SIT, PEN, WAS, PIN, CAN, ZIP, AIR, ARM, AID, GET, TIP, FOG, APP, HOT, BAR, SON, SEA, NOV, HUB, ACT, FOR, CAR, OUT, NOT, AIM, CAN, SEA, PDF, VIA, bet, FAN, HOT, PEN, LAB, ECM, not: 49개

최종적으로 127,985 - ( 18 + 49 ) = 127,918의 문자열을 가지고 다음 단계를 진행하였다.

### 3.4 Gene의 symbol과 alias를 PubMed 논문에서 
전 단계에서 선정한 127,918개의 문자열과 602,372 논문의 Abstract와 비교하였다. 이렇게 논문마다 등장하는 gene의 종류, 빈도를 계산하였다. 결과물에 대한 파일을 다음과 같다.

[allrDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6914686/allrDB_count.txt)

[nervDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6914687/nervDB_count.txt)

[respDB_count.txt](https://github.com/Deserav/Environmental-Disease/files/6916625/respDB_count.txt)


마지막으로 질환군별로 등장하는 gene과 alias를 파악하고, 개수를 확인하였다. 

[allrDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6915328/allrDB_gene_set.txt)

[nervDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6915327/nervDB_gene_set.txt)

[respDB_gene_set.txt](https://github.com/Deserav/Environmental-Disease/files/6916632/respDB_gene_set.txt)

그 결과, 질환군별로 나타나는 gene + alias 의 개수는 알레르기 질환군 5,215개, 신경계 질환군 12,739개, 호흡계 질환군 8,515 개였다.

