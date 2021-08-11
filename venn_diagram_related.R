# Get library
library(nVennR)
library(rsvg)
library(grImport2)

# First we read our dataframe file
df<-read.table(file="D:/Desktop/scrapy/gene_disease_link/gene_disease_original.txt", sep ="\t",  header=T)

COPD<-unique(subset(df, Disease == "Chronic obstructive pulmonary disease")$Original_Gene)
asthma<-unique(subset(df, Disease == "Asthma")$Original_Gene)
IPF<-unique(subset(df, Disease == "Idiopathic pulmonary fibrosis")$Original_Gene)
CF<-unique(subset(df, Disease == "Cystic fibrosis")$Original_Gene)

ADHD<-unique(subset(df, Disease == "Attention deficit hyperactivity disorder")$Original_Gene)
autism<-unique(subset(df, Disease == "Autism spectrum disorder")$Original_Gene)

MS<-unique(subset(df, Disease == "Multiple sclerosis")$Original_Gene)
PML<-unique(subset(df, Disease == "Progressive multifocal leukoencephalopathy")$Original_Gene)

myV<- plotVenn(list("COPD(652)"=COPD, "Asthma(905)" = asthma, "IPF(330)" = IPF, "CF(284)" = CF), nCycles = 2000, outFile = "D:/Desktop/resp.svg")
myV1<- plotVenn(list("ADHD(175)"=ADHD, "Autism(345)" = autism), nCycles = 2000, outFile = "D:/Desktop/nerv.svg")
myV <- plotVenn(list("MS(828)"=MS, "PML(31)"= PML), nCycles = 2000, outFile = "D:/Desktop/brain.svg")

print(length(COPD))
print(length(asthma))
print(length(IPF))
print(length(CF))

print(length(ADHD))
print(length(autism))

print(length(MS))
print(length(PML))