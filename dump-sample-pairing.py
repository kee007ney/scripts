#!/usr/bin/python
import os,sys
import string
import cgi
import commands
from optparse import OptionParser
import json

import csv
import glob


__version__="1.0"
__status__ = "Dev"

"""
This script has three options, you can execute the script in three ways:

1. python dump-sample-pairing.py --version
This is the option that show you the program's version.

2. python dump-sample-pairing.py -h
This can show you some help information.

3. python dump-sample-pairing.py -i xxx.fasta
This will check the .fasta file that if there are duplicate IDs in the sequence. 
If yes, it will output "Id repeated: bad fasta file".
If no, it will output the number of sequence.

"""
#~~~~~~~~~~~~~~~~~~~~~
def main():

	usage = "\n%prog  [options]"
        parser = OptionParser(usage,version="%prog " + __version__)
        parser.add_option("-r","--rsrcname",action="store",dest="rsrcname",help="Source name")

        (options,args) = parser.parse_args()
        for file in ([options.rsrcname]):
                if not (file):
                        parser.print_help()
                        sys.exit(0)

        rsrcName = options.rsrcname

       
	dataDir = "/data/projects/bioxpress/v-2.1/downloads/"+rsrcName+"/RNAseq/"
	outDir = "/data/projects/bioxpress/v-2.1/generated/extractor/" 
	pattern = dataDir + "*__gene_RNAseq__*.txt"
	tsvFileList = glob.glob(pattern)
	for tsvFile in tsvFileList:
		fileName = os.path.basename(tsvFile) 
		cancerType = fileName.split("_")[0]
		outFile = outDir + rsrcName + "-" + cancerType + "-samplepairing.csv"
		fieldList = []
		with open(tsvFile, 'rb') as FR:
			csvGrid = csv.reader(FR, delimiter='\t', quotechar='|')
			for row in csvGrid:
				fieldList = row
				break
		seen = {}
		sampleGrid = {}
		sampleid2index = {}
		sampleid2tissuetype = {}	
		for i in xrange(1,len(fieldList)):
			if fieldList[i] not in seen:
				sampleid2index[fieldList[i]] = i
				subjectId = "-".join(fieldList[i].split("-")[0:3])
				tissueId = fieldList[i].split("-")[3][0:-1]
				tmStatus = "normal" if tissueId == '11' else "tumor"
				if subjectId not in sampleGrid:
					sampleGrid[subjectId] = {"normal":[], "tumor":[]}
				sampleGrid[subjectId][tmStatus].append(fieldList[i])
			seen[fieldList[i]] = 1
	

		sampleList1 = []
		sampleList2 = []
		txtBuffer = ""
		for subjectId in sampleGrid:
			if len(sampleGrid[subjectId]["normal"]) > 0:
				for sampleId1 in sampleGrid[subjectId]["normal"]:
					for sampleId2 in sampleGrid[subjectId]["tumor"]:
						txtBuffer += "%s,%s,%s\n" % (subjectId,sampleId1,sampleId2) 	
						sampleList1.append(sampleId1)
						sampleList2.append(sampleId2)
		if len(sampleList1) > 0:
			with open(outFile, "w") as FW:
				FW.write("%s" % (txtBuffer))





if __name__ == '__main__':
        main()



