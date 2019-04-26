import subprocess
import argparse
import re


def Main():
    listOfArguments = []
    parser = argparse.ArgumentParser(description="This script calls annovar")
    parser.add_argument('--avinput', nargs='?')  ## User avinput

    parser.add_argument('--buildver', nargs='?')  ## human genome version we use hg19
    parser.add_argument('--out', nargs='?')  ## name of output file
    parser.add_argument('--remove', nargs='?')
    parser.add_argument('--protocol', nargs='?')  ##  database name for hg19_.
    parser.add_argument('--operation',
                        nargs='?')      ## operation type. g for gene-based, f for filter-based annotation
    parser.add_argument('--humandbDirPath', nargs='?')  ## databases location

    parser.add_argument('--nastring', nargs='?')

    parser.add_argument('--csvout', nargs='?')  ##create csv output
    parser.add_argument('--polish', nargs='?')
    parser.add_argument('--xreffile', nargs='?')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    Main()


def annotateWithTableAnnovar():
    allArgsReturned = []
    allArgsReturned = Main()  
    avinputReturned = allArgsReturned.avinput  

    allProtocols = allArgsReturned.protocol
    allTypesOfOperation = allArgsReturned.operation
    humanDbDirPath = allArgsReturned.humandbDirPath
    buildVer = allArgsReturned.buildver
    nameOfOutput = allArgsReturned.out
    xRefPath = allArgsReturned.xrefPath
    typeOfOperation = []
    allTypesOfOperationSplit = re.split(',',
                                        allTypesOfOperation)  ## The --operation needs to be separated by commas : refGene,dbnsfp35a
    
    allProtocolsSplit = re.split(',', allProtocols)
    allTypesOfOperationSplitAsString = ','.join(
        allTypesOfOperationSplit)
    allProtocolsSplitAsString = ','.join(allProtocolsSplit)
    print("operation type")
    print(str(
        allTypesOfOperationSplitAsString))
    print("protocol type or annotation name")
    print(str(allProtocolsSplitAsString))
    annovarScriptToExecute = (
                "perl table_annovar.pl " + avinputReturned + "test.avinput " + humanDbDirPath + " -buildver " + buildVer + " -out "
                + nameOfOutput + " -remove " + " -protocol " + str(allProtocolsSplitAsString) + " -operation " + str(
            allTypesOfOperationSplitAsString) + " -nastring " + "." + " -csvout" + "-polish" + "-xreffile" + xRefPath)
    print(annovarScriptToExecute)  ##  to execute perl commands
    subprocess.call(annovarScriptToExecute,
                    shell=True)
    return 0



"""
A script for coding variant annotation:

table_annovar.pl test.avinput humandb/ -buildver hg19 -out mycoding -remove -protocol refGene,dbnsfp35a,clinvar_20180603 -operation g,f,f
 -nastring . -csvout -polish -xreffile example/gene_fullxref.txt
 
A script for splice variant annotation:

table_annovar.pl test.avinput humandb/ -buildver hg19 -out mysplice -remove -protocol refGene,spidex, dbscsnv11 -operation g,f,f
 -nastring . -csvout -polish -xreffile example/gene_fullxref.txt
 

Before running the script download these databases individually:
# annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 dbnsfp35a humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 clinvar_20180603 humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 dbscnv11_genome humandb/


all downloaded databases should be in humandb file in annovar file
Spidex should be downloaded manually from annovar website and should be put in humandb file, too.
input file should be in .avinput format   : test.avinput
output file will be generated as .csv file  : mycoding.csv  or mysplice.csv
Important: python and perl scripts need to be in same direction
"""


annotateWithTableAnnovar()
