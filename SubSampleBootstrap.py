#! /usr/bin/env python

import os
import glob
import itertools
import dendropy
import subprocess
import shutil

def file_len(fName):
    with open(fName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

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
                        tree = (i.split()[0])
                        sub_tree = dendropy.Tree.get(data=tree, schema='newick', preserve_underscores=True)
                        sub_tree_list.append(sub_tree)
                    print("subsampled trees  - "+str(len(sub_tree_list)))
                    return sub_tree_list
        elif numTrees <= total_trees*counter:
            print(t+" is too short")
    elif min(file_len(t), numTrees, counter, stop) <= 0:
            print(t+" your variables are wrong")

def iterate_files(mainDir,suffix,nuGenNum,burnIn,outFolder):
    os.chdir(mainDir)
    for t in glob.glob("*.boottrees"):
        fName=t.rsplit(".", 1 )
        fName=fName[0]
        outPath=os.path.join(outFolder,fName+"_"+str(nuGenNum)+".t")
        treez = subsample_trees(t,burnIn,nuGenNum)
        treez.write(path=outPath, schema='nexus')
    os.chdir(mainDir)

# grab tree file
mainDir= "/Users/ethanbartel/Desktop/Bootstrap/gene_trees_subsampled_iq_all/Boottrees/"
suffix='.boottrees'
nuGenNum=10
burnIn=0
outFolder="/Users/ethanbartel/Desktop/Bootstrap/OutFolder"
iterate_files(mainDir,suffix,nuGenNum,burnIn,outFolder)
