import sys

sourcePath = sys.argv[1]
destPath   = sys.argv[2]

inputFile  = open(sys.argv[1],mode='r')
outputFile = open(sys.argv[2],mode='w')
numcases = int(inputFile.readline())
for casenum in range(1,numcases+1):
  result = inputFile.readline() 
  outputFile.write("Case #" + str(casenum) + " : " + str(result))