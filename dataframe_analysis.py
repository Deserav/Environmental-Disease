import pandas as pd
from collections import defaultdict

# Start from our dataframe
df = pd.read_csv("D:/Desktop/scrapy/gene_disease_link/gene_disease_original.txt", sep = "\t", usecols = ["Disease", "Original_Gene"])


disease_bio_type = {} # Our main dictionary. Keys are disease, and values are genes
disease_bio_num = []
bio_type_list = []

records = df.to_records(index=False) # Make our dataframe as a list of tuples and save it to result
result = list(records)

# The first loop makes our dictionary. Keys are disease and value are list of genes
for i in result:
    if i[0] not in disease_bio_type:
        disease_bio_type[i[0]] = [i[1]]
    else:
        disease_bio_type[i[0]].append(i[1])

# The value list has duplicates. The second loop removes duplicates
for key in disease_bio_type:
    disease_bio_type[key] = list(dict.fromkeys(disease_bio_type[key]))

# The third loop makes list of tuples of disease and count. It is easy to make dataframe this way
for key, value in disease_bio_type.items():
    disease_bio_num.append(tuple([key, len(value)]))

for key, value in disease_bio_type.items():
    bio_type_list.append(tuple([key, value]))

print(bio_type_list)
# print(disease_bio_num)

df1 = pd.DataFrame(disease_bio_num, columns = ["Disease", "Count"])
df1.to_csv("D:/Desktop/scrapy/gene_disease_link/number_of_biomarker_per_disease.txt", sep = "\t", index = False)

df2 = pd.DataFrame(bio_type_list, columns = ["Disease", "Biomarkers"])
df2.to_csv("D:/Desktop/scrapy/gene_disease_link/types_of_biomarker_per_disease.txt", sep = "\t", index = False)
