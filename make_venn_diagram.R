# First we read our dataframe file
df<-read.table(file="D:/Desktop/scrapy/gene_disease_link/gene_disease_original.txt", sep ="\t",  header=T)

# Load our library of package venn
library(ggvenn)

# Now we make our vector of biomarkers
allergy<-c()
nerve<-c()
respire<-c()
adhd<-c()

for(row in 1:nrow(df)){
  temp<- df[row, "Category"]
  if(temp == "Allergy"){
    allergy<-c(allergy, df[row, "Original_Gene"])
  } else if(temp == "Nerve"){
    nerve<-c(nerve, df[row, "Original_Gene"])
  } else if(temp == "Respire"){
    respire<-c(respire, df[row, "Original_Gene"])
    } else {adhd<-c(adhd, df[row, "Original_Gene"])}
  }

print(length(allergy))
print(length(nerve))
print(length(respire))
print(length(adhd))

# We remove duplicates by using 'unique()'. 
# It gets uniqe elements
allergy<-unique(allergy)
nerve<-unique(nerve)
respire<-unique(respire)
adhd<-unique(adhd)

print(length(allergy)) # 1086
print(length(nerve)) # 2362
print(length(respire)) # 2041
print(length(adhd)) # 175

a<-list(Allr = allergy, Nerv = nerve, Resp = respire, ADHD = adhd)
ggvenn(a)