import csv

"""
This script will output an array. 
This array contains the elements which is the product of the third row and the fourth row,
and it will ignore the first row(because it is normally titles for the rows) 
"""


FR = open("test.csv", "r")
data_frame = csv.reader(FR, delimiter=',', quotechar='"')
row_count = 0
for row in data_frame:
    row_count = row_count + 1
    if row_count == 1:
        continue
    new_row = row
    bmi = float(row[2])*float(row[3])
    new_row.append(bmi)
    print (new_row)
FR.close()

