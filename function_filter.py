## filtering the protein functionality analysis-annovar file
## This tool modifies the output file

import pandas as pd
df = pd.read_csv('C:\\')  #enter annovar output file as an input for filtering

#df=df.rename(columns = {'Otherinfo':'ID'})

                                                          #select specific columns

df = df[['Chr', 'Start', 'End', 'Ref', 'Alt', 'Func.refGene', 'Gene.refGene', 'ExonicFunc.refGene', 'AAChange.refGene',
         'Gene_full_name.refGene', 'SIFT_score', 'SIFT_converted_rankscore', 'SIFT_pred', 'Polyphen2_HDIV_score',
         'Polyphen2_HDIV_rankscore', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_score', 'Polyphen2_HVAR_rankscore',
         'Polyphen2_HVAR_pred', 'FATHMM_score', 'FATHMM_converted_rankscore', 'FATHMM_pred', 'CADD_raw',
         'CADD_raw_rankscore', 'CADD_phred', 'CLNALLELEID', 'CLNDN', 'CLNDISDB', 'CLNREVSTAT', 'CLNSIG', 'Otherinfo']]


remove_word = ['comment:']                                            ###remove 'comments: ' from string
pat = r'\b(?:{})\b'.format('|'.join(remove_word))

df['ID'] = df['Otherinfo'].str.replace(pat, '')                         ###column name change to 'ID'
del df['Otherinfo']

cols = df.columns.tolist()                                              ### move 'ID' column as a first column
cols = cols[-1:] + cols[:-1]
df = df[cols]

mask =df['ExonicFunc.refGene'].str.contains("nonsynonymous SNV")        ### select specific rows
df = df[mask]
"""
deleted columns:

del df['GeneDetail.refGene', 'pLi.refGene', 'pRec.refGene', 'pNull.refGene', 'pNull.refGene', 'Function_description.refGene',
       'Disease_description.refGene', 'Tissue_specificity(Uniprot).refGene', 'Expression(egenetics).refGene',
       'Expression(GNF/Atlas).refGene', 'P(HI).refGene', 'P(rec).refGene', 'RVIS.refGene', 'RVIS_percentile.refGene',
       'GDI.refGene', 'GDI-Phred.refGene', 'LRT_score', 'LRT_converted_rankscore', 'LRT_pred', 'MutationTaster_score',
       'MutationTaster_converted_rankscore', 'MutationTaster_pred', 'MutationAssessor_score', 'MutationAssessor_score_rankscore',
       'MutationAssessor_pred', 'PROVEAN_score', 'PROVEAN_converted_rankscore', 'PROVEAN_pred', 'VEST3_score', 'VEST3_rankscore',
       'MetaSVM_score', 'MetaSVM_rankscore', 'MetaSVM_pred', 'MetaLR_score', 'MetaLR_rankscore', 'MetaLR_pred', 'M-CAP_score',
       'M-CAP_rankscore', 'M-CAP_pred', 'REVEL_score', 'REVEL_rankscore', 'MutPred_score', 'MutPred_rankscore', 'DANN_score',
       'DANN_rankscore', 'fathmm-MKL_coding_score', 'fathmm-MKL_coding_rankscore', 'fathmm-MKL_coding_pred',
       'Eigen_coding_or_noncoding', 'Eigen-raw', 'Eigen-PC-raw', 'GenoCanyon_score', 'GenoCanyon_score_rankscore',
       'integrated_fitCons_score', 'integrated_fitCons_score_rankscore', 'integrated_confidence_value', 'GERP++_RS',
       'GERP++_RS_rankscore', 'phyloP100way_vertebrate', 'phyloP100way_vertebrate_rankscore', 'phyloP20way_mammalian',
       'phyloP20way_mammalian_rankscore', 'phastCons100way_vertebrate', 'phastCons100way_vertebrate_rankscore',
       'phastCons20way_mammalian', 'phastCons20way_mammalian_rankscore', 'SiPhy_29way_logOdds', 'SiPhy_29way_logOdds_rankscore',
       'Interpro_domain', 'GTEx_V6p_gene', 'GTEx_V6p_tissue']
"""


df.to_csv('C:\\', index= False)      #produce a modified output file without indexing




