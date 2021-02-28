#!/usr/bin/env python
# coding: utf-8

# ## 1
# Рассчитать экзонные длины генов GNG4 и SPRR4.Перекрывающиеся участки считать один раз: например, еслиэкзон 1 имеет координаты от 1 до 10, а экзон 2 имеет координатыот 7 до 15, то суммарная экзонная длина равна 15.

# In[12]:


import pandas as pd
import numpy as np

TSV1 = 'GNG4_exons.tsv'
TSV2 = 'SPRR4_exons.tsv'
GNG4 = pd.read_csv(TSV1, sep='\t')
SPRR4 = pd.read_csv(TSV2, sep='\t')

GNG4.columns =['chr', 'Annotation', 'exon', 'pos1', 'pos2', '1', '2', '3', 'id'] 
GNG4 = GNG4.sort_values(by='pos1')

c = GNG4.iloc[0]['pos2']
pos = GNG4.iloc[0]['pos1']
i = 1
for index, row in GNG4.iterrows():
    if row['pos2'] != c:
        print('Exon', i, 'length from GNG4 = ', c - pos)
        c = row['pos2']
        pos = row['pos1']
        i += 1

print('')
SPRR4.columns =['chr', 'Annotation', 'exon', 'pos1', 'pos2', '1', '2', '3', 'id'] 
SPRR4 = SPRR4.sort_values(by='pos1')

m = SPRR4.iloc[0]['pos2']
poss = SPRR4.iloc[0]['pos1']
i = 1
for index, row in SPRR4.iterrows():
    if row['pos2'] != c:
        print('Exon', i, 'length from SPRR4 = ', m - poss)
        m = row['pos2']
        poss = row['pos1']
        i += 1


# ## 2, 3
# 
# Написать программу для расчета нормировочных множителейметодом median-of-ratios (без использования модуля DESeq2).Проверить работоспособность на файле TCGA; эталонный ответ,рассчитанный с помощью DESeq2: 0.35219656, 0.39439086,0.73057344, 1.66138079, 1.60002838, 1.48313616, 1.28046971,0.92434274, 1.59306799, 1.34997698. Hint: для подсчета среднегогеометрического использовать среднее арифметическоелогарифмов.

# In[9]:


import pandas as pd
from scipy import stats

df = pd.read_csv('TCGA-COAD_cancer_normal.tsv', sep='\t', index_col=0)
df = df.replace(0, pd.np.nan)
df = df.dropna(axis=0, how='any')

df['Geometric Mean'] = stats.gmean(df.iloc[:, 0:10], axis=1) 

df_ratio = df.div(df['Geometric Mean'], axis=0)
df_ratio = df_ratio.drop(['Geometric Mean'], axis=1)

med = (df_ratio.median(axis=0)).to_list()
samples = df_ratio.columns.to_list()
graph = pd.DataFrame(
    {'Samples': samples,
     'Median': med})
ax = graph.plot.bar(x='Samples', y='Median', color=['#ff355e'])


# ## 4

# In[11]:


import pandas as pd
import numpy as np

# classwork 
df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()

RPM = df.div(df.sum(axis=0) / 10**6, axis=1)
RPKM = RPM.div(gl["Length"] / 10**3, axis=0)

size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 1.60002838, 
                1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698]
RPKM = RPKM.div(size_factors, axis=1)

df = np.log2(RPKM + 1)
df = df.loc[df.max(axis=1) > 0]
df["median"] = df.median(axis=1)
df = df.sort_values("median", ascending=False)
df = df.iloc[:len(df)//2]

# normalized dataframe
df_norm = df.div(df['median'], axis=0)

df["LFC"] = df.iloc[:, 0:5].mean(axis=1) - df.iloc[:, 5:10].mean(axis=1)
df["absLFC"] = np.abs(df["LFC"])
df = df.sort_values("absLFC", ascending=False)


df_norm["LFC"] = df_norm.iloc[:, 0:5].mean(axis=1) - df_norm.iloc[:, 5:10].mean(axis=1)
df_norm["absLFC"] = np.abs(df_norm["LFC"])
df_norm = df_norm.sort_values("absLFC", ascending=False)

# choosing top genes
TOP = df['absLFC'].head(100).to_frame()
TOP_norm = df_norm['absLFC'].head(100).to_frame()

# couldn't get genes' names with genes as rows indexes :( Therefore...
TOP.reset_index(level=0, inplace=True)
TOP_norm.reset_index(level=0, inplace=True)

# making dataframes with top genes from both dataframes (norm and non-norm data)
top = TOP['Gene'].to_frame()
topn = TOP_norm['Gene'].to_frame()
merge = top.merge(topn)
# merge
# making lists for dataframe for scatterplot
merge_genes = ['CST1', 'KRT8P36', 'KRT23', 'KLK10', 'VWA2', 'MT-TM', 'CLDN2']
TOP_gr = TOP.loc[TOP['Gene'].isin(merge_genes)]
TOP_ngr = TOP_norm.loc[TOP['Gene'].isin(merge_genes)]
t_list = TOP_gr['absLFC'].tolist()
tn_list = TOP_ngr['absLFC'].tolist()

plot = pd.DataFrame(
    {'Genes': merge_genes,
     'normalized': tn_list,
     'non-normalized': t_list})
#print(plot)

import seaborn as sns
print(sns.scatterplot(data=plot, x="normalized", y="non-normalized", color=['#ff355e']))


# ## 5

# In[145]:


import pandas as pd
import numpy as np

df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()

RPM = df.div(df.sum(axis=0) / 10**6, axis=1)
RPKM = RPM.div(gl["Length"] / 10**3, axis=0)

size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 1.60002838, 1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698]
RPKM = RPKM.div(size_factors, axis=1)

df = np.log2(RPKM + 1)
df = df.loc[df.max(axis=1) > 0]
df["median"] = df.median(axis=1)
df = df.sort_values("median", ascending=False)
df = df.iloc[:len(df)//2]

df_norm = df.div(df['median'], axis=0)

df["LFC"] = df.iloc[:, 0:5].mean(axis=1) - df.iloc[:, 5:10].mean(axis=1)
df["absLFC"] = np.abs(df["LFC"])
df = df.sort_values("absLFC", ascending=False)

df_norm["LFC"] = df_norm.iloc[:, 0:5].mean(axis=1) - df_norm.iloc[:, 5:10].mean(axis=1)
df_norm["absLFC"] = np.abs(df_norm["LFC"])
df_norm = df_norm.sort_values("absLFC", ascending=False)

df_std = df.drop(['median'], axis=1)
df_std = df_std.drop(['LFC'], axis=1)
df_std = df_std.drop(['absLFC'], axis=1)
df_std['der'] = df_std.std(axis=1)

df_nstd = df_norm.drop(['median'], axis=1)
df_nstd = df_nstd.drop(['LFC'], axis=1)
df_nstd = df_nstd.drop(['absLFC'], axis=1)
df_nstd['der'] = df_nstd.std(axis=1)

df_nstd['der'] = df_nstd.std(axis=1)

TOP = df_std['der'].tail(10).to_frame()
TOP_norm = df_nstd['der'].tail(10).to_frame()
TOP.reset_index(level=0, inplace=True)
TOP_norm.reset_index(level=0, inplace=True)

top = TOP['Gene'].to_frame()
topn = TOP_norm['Gene'].to_frame()
merge = top.merge(topn)
print(merge)


# In[ ]:




