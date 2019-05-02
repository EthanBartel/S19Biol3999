#! /usr/bin/env python

import os
import glob
import itertools
import dendropy
import subprocess
import shutil
import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    print(i+1)
    print(fName)

def subsample_trees(t,burn,total_trees):
	# For RevBayes we also use this to delete the header file
	rb_burnin = burn + 1
	# Get number of trees in post-burnin sample
	numTrees = file_len(t) - rb_burnin
	# Sampler counter
	counter = int(numTrees/total_trees)
	# When to stop
	stop = int(total_trees*counter + rb_burnin)
	#debug
	variables = [file_len(t),total_trees,numTrees,counter,rb_burnin,stop]
	print("numbers for debugging - " + str(variables))
	#check if there are enough trees in file
	if min(file_len(t), numTrees, counter, stop) > 0:
		if numTrees > total_trees*counter:
			#check dendropy version
			version=dendropy.__version__.split(".")[0]
			if version == '4':
				#open tree file, create output file name, initiate dendropy tree list
				with open(t) as trees:
					sub_tree_list = dendropy.TreeList()
					#iterate through lines in file, split out newick string, transform to tree object, add to tree list
					print(t + " - reading in files...")
					for i in itertools.islice(trees, rb_burnin, stop, counter):
						# column to read from.
						tree = (i.split()[5])
						sub_tree = dendropy.Tree.get(data=tree, schema='newick', preserve_underscores=True)
						sub_tree_list.append(sub_tree)
					print("subsampled trees  - "+str(len(sub_tree_list)))
					return sub_tree_list
		elif numTrees <= total_trees*counter:
			print(t+" is too short")
	elif min(file_len(t), numTrees, counter, stop) <= 0:
			print(t+" your variables are wrong")

def iterate_files(mainDir,fileList,suffix,nuGenNum,burnIn,outFolder):
	os.chdir(mainDir)
	# if no subset file list is passed, use all files.
	if len(fileList) == 0:
		# repopulate file list with all files.
		fileList = []
		for f in glob.glob('%s*%s' % (suffix)):
			fileList.append(f)
	# Iterate through file list.
	for n in fileList:
		# Get base name of file
		nexus=str(n);print(n)
		nexusIndex = nexus.find(suffix)
		fName = nexus[:nexusIndex]
		# Get path to output posterior files.
		outputPath = os.path.join(mainDir,fName,"OutFolder/")
		# Move into rb output path
		os.chdir(outputPath)
		print(os.getcwd())
		# Iterate through files
		for t in glob.glob('*.treefile'):
			outPath=os.path.join(outFolder,fName+"_"+str(nuGenNum)+"_dp.nex")
			treez = subsample_trees(t,burnIn,nuGenNum)
			treez.write(path=outPath, schema='nexus')
		os.chdir(mainDir)

def subSampleLoci(suffix,prefixDict,mainDir):
	os.chdir(mainDir)
	subSetFolderNames=[]
	# Iterate through dictionary
	for p,n in prefixDict.items():
		allFileList=[]
		for f in glob.glob('%s*%s' % (p,suffix)):
			allFileList.append(f);print(allFileList)
		subSetFolderNames.extend(random.randrange(allFileList,int(n)))
	return subSetFolderNames
# grab tree file

# Iterate through folders in main directory
mainDir1="/Users/ethanbartel/Desktop/Bootstrap/gene_trees_subsampled_iq_all"
# Use nexus files outside folders to iterate through folders
suffix=".prg.nex"
# Subsample this many trees PER locus file
nuGenNum=10
# No burnin
burnIn=0
# Where to place new files
outFolder="/Users/ethanbartel/Desktop/Bootstrap/OutFolder"

prefixDict={'AHE':23,'gene':7}
fileList=subSampleLoci(suffix,prefixDict,mainDir1)
print(fileList)
iterate_files(mainDir1,fileList,suffix,nuGenNum,burnIn,outFolder)
