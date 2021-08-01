# Complete program File
# The base is from abstract_to_gene.py at D:/Desktop/scrapy/Genes/abstract_to_gene.py
# Gene name is extracted from D:/Desktop/scrapy/Genes/filterDB.csv, not gen_ali.txt
# Disease filenames are extracted from : 민규 파일이름
import datetime
import os
import matplotlib.pyplot as plt

category = ["allrDB", "nervDB", "respDB"] # Database categories used in the research
genes = []

f2 = open("D:/Desktop/scrapy/Genes/final_genelist.txt", "r") # fixed: genes without common words ex: not, nan
x = f2.readlines()
for ele in x:
    genes.append(ele.strip())

# genes = f2.read().split(",") # fixed

par = [] # Gene list with parenthesis
norm = [] # Gene list without parenthesis
del_par = [] # The list that has elements of list "par" without parenthesis

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
# print(del_par)
# Delete parenthesis of genes in par : del_par

begin_time = datetime.datetime.now()
print("Program starts at: ", datetime.datetime.now().strftime("%X")) # Time that the program is started
for database in category:
    f0 = open("D:/Desktop/scrapy/Pubmed/{}_shredded_list.txt".format(database), "r") # 질병 목록파일
    z = f0.readlines() #한줄씩 읽기

    for disease in z:
        gene_appeared = [] # temporary List of genes that appear in every disease. Has duplicates so will be made to dictinary
        freq_gene_appeared = {} # Dictionary of genes and the number of appearance.
        a = disease.replace("  \n", "").strip() # Disease name from file z has space and \n in it. We delete it with strip()
        f = open("D:/Desktop/scrapy/PubMed/{}_final/{}.txt".format(database, a), "r") # Open files with the format 'database' and 'a'
        y = f.readlines()
        print("File '{}' is read".format(a), "Time:", datetime.datetime.now().strftime("%X")) # Shows the time when a new file is read

        print("Time lapse: ", datetime.datetime.now()-begin_time)
        f2 = open("D:/Desktop/scrapy/PubMed/{}_output/{}_output.txt".format(database,a), "w")
        f2.close()
        print("File '{}_output' is made.".format(a))
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
                if len(templist) != 0: # Return result when list is not empty
                    write_f2 = open("D:/Desktop/scrapy/PubMed/allrDB_output/{}_output.txt".format(a), "a")
                    write_f2.write(y[index - 1])
                    write_f2.write(y[index])
                    write_f2.write(y[index + 1])
                    write_f2.write("Genes found: "+ str(set(templist)) + "\n\n")
                    write_f2.close()
                    print("Paper title: ", y[index - 1])
                    print("Abstract: ", y[index])
                    print(y[index + 1])
                    print("Genes found: ", str(set(templist))) # Make templist to set to delete duplicates
                    print("")

        for ele in gene_appeared:
            if ele in freq_gene_appeared:
                freq_gene_appeared[ele] += 1
            else:
                freq_gene_appeared[ele] = 1
        plt.figure(figsize = (15, 6), dpi = 250) # Adjust size and resolution of plot
        plt.bar(range(len(freq_gene_appeared)), freq_gene_appeared.values(), align='center')

        if len(gene_appeared) < 15:
            plt.xticks(range(len(freq_gene_appeared)), list(freq_gene_appeared.keys()))
        else:
            plt.xticks(range(len(freq_gene_appeared)), list(freq_gene_appeared.keys()), fontsize = 3, rotation = 90) # Fontsize default is 12, rotation default is 0

        plt.title('{}'.format(a))
        plt.xlabel('Gene Name')
        plt.ylabel('Frequency')
        plt.savefig('D:/Desktop/scrapy/PubMed/allrDB_output/{}_output.png'.format(a))
        # plt.show()

        f3 = open("D:/Desktop/scrapy/PubMed/allrDB_output/{}_output.txt".format(a), "a")
        f3.write("Number of genes found: " + str(len(set(gene_appeared))) + "\n")
        f3.write("Genes appeared in disease '{}' : ".format(a) + str(set(gene_appeared)) + "\n\n")
        f3.write("Frequency of gene appearance: " + str(freq_gene_appeared))
        f3.close()
