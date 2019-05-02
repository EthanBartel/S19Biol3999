##!/usr/bin/env python
#NonCharset lines
import re
NexFile=("/Users/ethanbartel/Downloads/nexus_files_concat/TestFile.nex")
with open(NexFile) as file:
    with open("TestOutFile.nex", "w") as out:
        for line in file:
        	out.write(str(line))

with open(NexFile) as file:
	head = [next(file) for x in range(26)]
	print(head)

with open(NexFile) as file:
    with open("OutFile.nex", "w") as out:
        for line in file:
        	num=re.search('(?<=:)(.*?)(?=,)',line)#sets numbers as "num"
			num=(num.group(1))
        	char=re.match('(.*?)(?=:)',line) #Sets letters as "char"
			char=(char.group(1))
			line=re.sub(num,char,line) #replaces numbers with char variable
			if ":" in line:
				out.write(line) #Write to file
#Charset Lines (I like this one better)
with open(NexFile) as file:
    with open("OutTemp.nex", "w+") as out:
        for line in file:
			num=re.search('(?<=\\=)(.*?)(?=\\;)',line)#sets numbers as "num"
			num=(num.group(1))
			char=re.search('(?<=t)(.*?)(?=\\=)',line)#sets letters as "char"
			char=(char.group(1))
			line=re.sub(num,char,line) #replaces num with char
			if "=" in line:
				out.write(line) #Write to file
