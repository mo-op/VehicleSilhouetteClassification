import csv
import sys

filePath = str(sys.argv[1])
fileName = str(sys.argv[2])

# # read flash.dat to a list of lists
datContent = [i.strip().split() for i in open(filePath).readlines()]

newFileName = fileName + ".csv"
# write it as a new CSV file
with open(newFileName, "a") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)

