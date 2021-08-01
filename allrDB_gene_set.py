f0 = open("D:/Desktop/scrapy/PubMed/allrDB_count.txt", "r")
x = f0.readlines()

disease = []
genes = []

for i in range(len(x)):
    if i % 7 == 0:
        disease.append(x[i][9:])
    elif i % 7 == 3:
        genes.append(x[i])
    else:
        pass

for i in range(len(genes)):
    if "{" in genes[i]:
        y = genes[i].index("{")
        genes[i] = genes[i][y + 1 : len(genes[i])]
    else:
        genes.remove(genes[i])



# print(disease)
# print(genes)
