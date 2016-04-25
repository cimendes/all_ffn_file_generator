import sys
import os

try:
	readsDirectory=sys.argv[1]
except IndexError: 
	print "Invalid input." #TODO
	raise SystemExit

allffnfile = open("allffnfile.fasta", "w")

currentDir=os.getcwd()

os.chdir(readsDirectory)

l=os.listdir(readsDirectory)

if not l:
	print "No directories found!"
	raise SystemExit

for item in l:
	for files in os.listdir(item):
		if files.endswith(".ffn"):
			ffnfile=open(item + "/" + files , "r")

			for line in ffnfile:
				allffnfile.write(line)
			ffnfile.close()

allffnfile.close()



