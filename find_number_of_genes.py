# category = ["allrDB", "nervDB", "respDB"] # Database categories used in the research
genes = []
par = []
norm = []
del_par = []

f2 = open("D:/Desktop/scrapy/Genes/final_genelist.txt", "r") # fixed: genes without common words ex: not, nan
x = f2.readlines()
for ele in x:
    genes.append(ele.strip())

for i in genes:
    if "nan" not in i and "(" in i:
        par.append(i)
# list of genes with parenthesis: par

for j in genes:
    if "nan" not in j and "(" not in j:
        norm.append(j)
# list of genes without parenthesis : norm

for k in par:
    del_par.append(k.replace("(", " ").replace(")", " ").strip())


# for database in category:
f0 = open("D:/Desktop/scrapy/Pubmed/respDB_shredded_list.txt" "r") # 질병 목록파일 줄인 file
z = f0.readlines()
fy = open("D:/Desktop/scrapy/Pubmed/respDB_count.txt", "w")
fy.close()

    for disease in z:
        gene_appeared = [] # temporary List of genes that appear in every disease. Has duplicates so will be made to dictinary
        freq_gene_appeared = {} # Dictionary of genes and the number of appearance.
        a = disease.replace("  \n", "").strip() # Disease name from file z has space and \n in it. We delete it with strip()
        f = open("D:/Desktop/scrapy/PubMed/respDB_final/{}.txt".format(a), "r") # Open files with the format 'database' and 'a'
        y = f.readlines()
        print("File '{}' is read".format(a)) # Shows the time when a new file is read
        # Find genes in abstract from norm:
        for index, line in enumerate(y):
            if index % 4 == 1:
                v = line.replace("(", " ").replace(")", " ") # Exchange parenthesis to space of abstract and store at temporary variable v
                templist = [] # Make a temporary list for each iterable
                    # print("Line {} is read".format(index))
                for words in v.split(): # Match each words of abstract with norm and append it to templist
                    if words in norm:
                        templist.append(words)
                        gene_appeared.append(words)
                        continue # Move to next so it doesn't count multiple encounters in paper.
                    elif words.strip() in del_par: # Match each words of abstract with del_par  and append it to templist
                        templist.append(words)
                        gene_appeared.append(words)
                        continue
                    else:
                        pass

        for ele in gene_appeared:
            if ele in freq_gene_appeared:
                freq_gene_appeared[ele] += 1
            else:
                freq_gene_appeared[ele] = 1
        # Make dictionary with frequency of gene appearance

        fx = open("D:/Desktop/scrapy/Pubmed/{}_count.txt".format(database), "a")
        fx.write("Disease: {}".format(disease) + "\n")
        fx.write("Number of genes found: " + str(len(set(gene_appeared))) + "\n")
        fx.write("Genes appeared in disease '{}' : ".format(a) + str(set(gene_appeared)) + "\n")
        fx.write("Frequency of gene appearance: " + str(freq_gene_appeared) + "\n\n\n")
