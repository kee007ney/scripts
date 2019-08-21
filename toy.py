import csv
"""

This script will use xxx.csv as an input and output all the rows with the row number.

"""

with open("A.csv", 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in csvreader:
		for j in xrange(0,len(row)):
			print (j,row[j])

