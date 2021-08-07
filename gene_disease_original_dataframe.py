# This program is very important as well.
# Essential enough to go in Key Program Files but for convenience it is saved here

import pandas as pd

# We use the dataframe of raw data from NCBI
df = pd.read_csv("D:/Desktop/scrapy/Genes/gene_result.txt", sep = "\t", usecols = ["Symbol", "Aliases"])

# First we make a dictionary of genes and aliases
gene_alias = {}

for i in range(len(df)):
    value_string = str(df.iat[i, 0]) + ", " + str(df.iat[i, 1])
    gene_alias[df.iat[i, 0]] = value_string.split(", ")
    # print(gene_alias)

for key in gene_alias:
    if 'nan' in gene_alias[key]:
        gene_alias[key].pop()

# Our dictionary of gene and aliases are perfectly made. The dataframe is not modified.
# Keys are symbol and values are symbol + aliases.

# From here we try to make our dataframe of [disease, category, match, original]
column_name = ["Disease", "Category", "Match", "Original_Gene"]

category = ["Allergy", "Nerve", "Respire", "ADHD"] # Our database

complete_list = [] # This will be a list of tuples with structure (disase, category, gene_or_alias, original)

# In count file, we have all disease names, but there are some lines that don't have genes
for ele in category:
    print(ele," is being started")
    f = open("D:/Desktop/scrapy/gene_disease_link/{}_count.txt".format(ele), "r") # We have four count files
    x = f.readlines()
    mid = [] # Make temporary list. Format is [disease, category, gene_or_alias, original]. Will be converted to tuple and added to complete_list
    for i in range(len(x)):
        if i % 7 == 3 and "{" in x[i]:
            start = x[i].index("{")
            last = x[i].index("}")
            gene_string = x[i][start + 1 : last].replace("'", "").replace(" ", "")
            disease = x[i - 3].replace("Disease: ", "").replace("\n", "").strip() # get rid of front and back
            for string in gene_string.split(","):
                for key in gene_alias:
                    temp = [] # List that will be used every loop
                    if string in gene_alias[key]:
                        temp.append(disease)
                        temp.append(ele)
                        temp.append(string)
                        temp.append(key)
                        mid.append(tuple(temp)) # convert list to tuples and send to mid
        else:
            continue
    for i in mid: # mid is now a list of tupples. now sent it to global list
        complete_list.append(i)

print(complete_list)
print("Dataframe is being made")
df2 = pd.DataFrame(complete_list, columns = column_name) # Make pandas datafram from complete_list
df2.to_csv('D:/Desktop/scrapy/gene_disease_link/gene_disease_original.txt', sep = '\t', index = False)
