import glob
import dendropy
import os
import random

def combineTrees(treeGuide,outPath,mainDir,fileExt):
    os.chdir(mainDir)
    treeList = dendropy.TreeList()
    fileList = []
    for f in glob.glob(fileExt):
            fileList.append(f)
    fileList.sort()
    fileList=random.sample(fileList, 7)
    counter=0
    for x in fileList:
        tList = dendropy.TreeList.get(file=open(x,"r"), schema='nexus', preserve_underscores=True)
        for t in tList:
            treeList.append(t)
            counter+=1
            # treeGuide.write("Tree "+str(counter)+", "+x+"\n")
            treeList.write(path=outPath, schema='nexus')
            treeGuide.close()

mainDir="/Users/ethanbartel/Desktop/Bootstrap/OutFolder/Gene/10"
# Start file to record order of trees
treeGuide=open(os.path.join(mainDir,"gene_trees.log"),"w")
# Write trees to here
outPath=os.path.join(mainDir,'gene_trees_60.nex')
# File extension for trees to be combined
fileExt="*.t"
combineTrees(treeGuide,outPath,mainDir,fileExt)
