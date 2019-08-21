import os,sys
import string
import json
from optparse import OptionParser
import csv
import glob

"""
This script use a .csv as input and output the fieldnames and field in the file.
"""
__version__="1.0"
__status__ = "Dev"


###############################
def main():



	pattern = "/data/projects/glygen/generated/output/*.csv"
	filePathList = glob.glob(pattern)

	seen  = {}
	for filePath in filePathList:
		fNames = os.path.basename(filePath)
		with open(filePath, 'r') as FR:
        		dataFrame = csv.reader(FR, delimiter=',', quotechar='"')
        		rowCount = 0
			for row in dataFrame:
				rowCount += 1
				if rowCount == 1:
					for field in row:
						if field not in seen:
							seen[field] = []
						seen[field].append(fNames)

	for field in seen:
		fNamess = seen[field]
		if len(fNamess) > 1:
			for i in xrange(0, len(fNamess)):
				for j in xrange(i, len(fNamess)): 
					o = "%s.%s,%s.%s" % (fNamess[i],field,fNames[j],field)
					print o


if __name__ == '__main__':
        main()


