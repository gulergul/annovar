
## filtering the protein functionality analysis-annovar file
## This tool modifies the output file

import pandas as pd
df = pd.read_csv('C:\\')  #enter annovar output file as an input for filtering

#df=df.rename(columns = {'Otherinfo':'ID'})

                                                          #select specific columns

df = df[['Chr', 'Start', 'End', 'Ref', 'Alt', 'Func.refGene', 'Gene.refGene', 'ExonicFunc.refGene', 'AAChange.refGene',
         'Gene_full_name.refGene', 'dbscSNV_ADA_SCORE', 'dbscSNV_RF_SCORE', 'dpsi_max_tissue', 'dpsi_zscore', 'Otherinfo']]

#, 'dbscSNV_ADA_SCORE', 'dbscSNV_RF_SCORE', 'dpsi_max_tissue', 'dpsi_zscore',
remove_word = ['comment']                                            ###remove 'comments: ' from string
pat = r'\b(?:{})\b'.format('|'.join(remove_word))

df['ID'] = df['Otherinfo'].str.replace(pat, '')                         ###column name change to 'ID'
del df['Otherinfo']

cols = df.columns.tolist()                                              ### move 'ID' column as a first column
cols = cols[-1:] + cols[:-1]
df = df[cols]


df.to_csv('C:\\', index= False)      #produce a modified output file without indexing








