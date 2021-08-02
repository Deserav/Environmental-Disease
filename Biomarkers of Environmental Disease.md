# 주제: PubMed을 이용한 환경성 질환의 biomarker 탐색
본 과제에서 NCBI 산하의 데이터베이스인 PubMed의 논문을 이용하여 환경성 질환에 대한 biomarker가 무엇이 있는지 알아보았다.

## 1. 목적
본 연구의 목적은 환경성 질환의 genetic biomarker를 찾고, 데이터베이스를 구축하는 것이다.

환경성 질환은 환경보건법 제2조 제 2호[1]에 따라 환경유해인자와 상관성이 있다고 인정되는 질환 중 감염질환이 아닌 것을 이야기한다. 본 보고서에는 6가지 환경성질환군 중에서 RFP에서 요구한
- 알레르기 질환군
- 신경계 질환군
- 호흡계 질환군

위 3가지에 대해서 연구를 진행하였다.

현재 선행연구 중에서 genetic biomarker과 disease가 키워드로 포함된 논문을 PubMed에서 찾아, 등장하는 gene과 disease 이름을 파악하여 관련성이 높은 것을 찾는 것이 목표이다.

## 2. 과정에 대한 Flowchart

## 3. Progress

### 3.1 ICD의 질병을 분류
ICD(International Statistical Classification of Diseases and Related Health Problems) [2] 는 세계보건기구에서 만든, 질병과 증후군에 대한 국제 표준이다. 본 연구에서 사용한 ICD-11는 ICD의 11번째 개정안으로, 2019년 5월에 채택되었고, 2022년 1월 1일부터 효력을 가진다. 

ICD-11에서 제시한 알레르기 질환, 신경계 질환, 호흡계 질환에 어떤 것이 있는지 파악하였다. 그리고 각 질병이 biomarker가 있는지 알아보기 위해, PubMed에서 (질병명[Title/Abstract]) AND (biomarker[Title/Abstract])의 키워드로 검색했을 때 등장하는 논문의 수를 알아보았다. 그 결과는 다음과 같다.

|         |알레르기 질환군| 신경계 질환군| 호흡계 질환군|
|---------|-------------|------------|-----------|
|총 질환 개수|385|2175|667|
|논문이 존재하는 질환의 개수|**149**|**652**|**215**|
|논문의 수|38,458|383,659|180,255|

### 3.2 PubMed에서 질병별 Title, Abstract, DOI 추출
Python의 Biopython 모듈로부터 Entrez와 Medline 모듈을 사용하여, 검색 키워드로부터 등장하는 논문들의 Title, Abstract, DOI를 전부 하나의 txt 파일로 정리하였다. 

ICD-11에서 찾은 개별적인 질명에 biomarker라는 키워드와 결합하여 (질병명[Title/Abstract]) AND (biomarker[Title/Abstract])로 검색하였다. 각 질병별 검색 결과로 나타나는 논문들의 Title, Abstract, DOI를 txt 파일로 정리하였다. 이런 식으로 알레르기 질환 149개, 신경계 질환 652개, 호흡계 질환 215개의 txt 파일을 만들었다.

### 3.3 NCBI에 있는 human gene database로 부터 각 논문별 등장하는 gene 파악
NCBI에 등장하는 63,816개의 (pseudogene, tRNA gene 등을 포함) gene의 symbol과 alias를 전부 추출하여, 질병 txt 파일의 Abstract와 비교하였다. 이렇게 등장하는 gene의 종류, 빈도를 파악하였다. 

그 결과 나타나는 gene의 개수는 알레르기 질환군 5,215개, 신경계 질환군 12,739개, 호흡계 질환군 x개가 나타났다.

