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
    allArgsReturned = Main()  ## whatever arguement user supplied  is stored as a list
    avinputReturned = allArgsReturned.avinput  ## access a particular arguement using the "dotArguementName" syntax
    ## Line 37-42 is similar syntax to line 36 and they will be inputs to call of annovar

    allProtocols = allArgsReturned.protocol
    allTypesOfOperation = allArgsReturned.operation
    humanDbDirPath = allArgsReturned.humandbDirPath
    buildVer = allArgsReturned.buildver
    nameOfOutput = allArgsReturned.out
    xRefPath = allArgsReturned.xrefPath
    typeOfOperation = []
    allTypesOfOperationSplit = re.split(',',
                                        allTypesOfOperation)  ## The --operation needs arguement separated by commas eg refGene,dbnsfp35a
    ## FOr line 44 I have followed annovar style of supplying arguements
    allProtocolsSplit = re.split(',', allProtocols)
    allTypesOfOperationSplitAsString = ','.join(
        allTypesOfOperationSplit)
    allProtocolsSplitAsString = ','.join(allProtocolsSplit)
    print("This is type of operation")
    print(str(
        allTypesOfOperationSplitAsString))
    print("These are the protocol/annotation type names")
    print(str(allProtocolsSplitAsString))
    annovarScriptToExecute = (
                "perl table_annovar.pl " + avinputReturned + "test.avinput " + humanDbDirPath + " -buildver " + buildVer + " -out "
                + nameOfOutput + " -remove " + " -protocol " + str(allProtocolsSplitAsString) + " -operation " + str(
            allTypesOfOperationSplitAsString) + " -nastring " + "." + " -csvout" + "-polish" + "-xreffile" + xRefPath)
    print(annovarScriptToExecute)  ## The actual perl script to be executed as a string
    subprocess.call(annovarScriptToExecute,
                    shell=True)
    return 0


def read_annotation(avinput_file):
    pass


if __name__ == "__main__":
    pass


"""
Sample script for coding variant annotation:

table_annovar.pl test.avinput humandb/ -buildver hg19 -out mycoding -remove -protocol refGene,dbnsfp35a,clinvar_20180603 -operation g,f,f
 -nastring . -csvout -polish -xreffile example/gene_fullxref.txt
 
Sample script for splice variant annotation:

table_annovar.pl test.avinput humandb/ -buildver hg19 -out mysplice -remove -protocol refGene,spidex, dbscsnv11 -operation g,f,f
 -nastring . -csvout -polish -xreffile example/gene_fullxref.txt
 

Before running the script download the database and create a folder called humandb in folder where your annovar perl scripts are
# annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 dbnsfp35a humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 clinvar_20180603 humandb/

# annotate_variation.pl -downdb -webfrom annovar -buildver hg19 dbscnv11_genome humandb/

Spidex should me downloaded manually
Put all databases in humandb
input file in .avinput format
Just check annovar's documentation for that
The way this script is know python script and perl script have to be in the same directory.
"""


annotateWithTableAnnovar()