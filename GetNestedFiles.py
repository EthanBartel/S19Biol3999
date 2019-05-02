#! /usr/bin/env python
import os
import shutil

RootDir1 = r'/Users/ethanbartel/Desktop/Bootstrap/'
TargetFolder = r'/Users/ethanbartel/Desktop/Bootstrap/gene_trees_subsampled_iq_all/'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.boottrees'):
                print("Found")
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder)


#If that works
# destination="/Users/ethanbartel/Desktop/Bootstrap/gene_trees_subsampled_iq_all/Boottrees"
# filetype="*.boottrees"
# os.mkdir(destination)
# os.mv(filetype destination)
