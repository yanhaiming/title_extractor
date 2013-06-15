#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:some useful functions.

import sys

#对文件按字符顺序进行排序
def sortFile(fileIn,fileOut):
	print '开始对文件进行排序...'
	fi = open(fileIn,'r')
	fo = open(fileOut,'w')

	strList = []
	for line in fi:
		strLine = line.strip('\n')
		strList.append(strLine)
		strList = sorted(strList)
	
	for item in strList:
		fo.write(item + '\n')

if __name__=='__main__':
	if len(sys.argv) != 3:
		print '<usage:> fileIn.txt fileOut_sorted.txt'
		exit(1)
	sortFile(sys.argv[1],sys.argv[2])

