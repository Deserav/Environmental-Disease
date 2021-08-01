# f0 = open("D:/Desktop/scrapy/PubMed/allrDB_count.txt", "r")
f0 = open("C:/Users/frigg/Desktop/Environmental-Disease-main/Environmental-Disease-main/allrDB_count.txt", "r")

x = f0.readlines()

disease = []
genes = []
final = []

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
        genes[i] = ""

for strings in genes:
    final.extend(strings.replace("'", "").replace("}", "").split())

# print(final)
omega = list(set(final))
print(len(omega)) # found a total of 5251 genes in "allrDB_count.txt"

f1 = open("C:/Users/frigg/Desktop/allrDB_gene_set.txt", "w")
y = f1.writelines(omega)
# print(final)
# print(disease)
# print(genes)
