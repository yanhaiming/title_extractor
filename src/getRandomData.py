#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:get some sample data from result set randomly.

import sys
import random

_sampleNum = 150
_resList = []
_MAX_NUM = 5 #一个类最多展示的个数

#从所生成的比价页中随机抽取一部分来进行指标评估.
#fileIn: indexPage_sorted.txt,即所生成的比价页.
#fileOut:随机抽取得到的结果.

def getRandomSample(fileIn,fileOut):
	fi = open(fileIn,'r')
	fo = open(fileOut,'w')
	for line in fi:
		_resList.append(line)
	fi.close
	iCount = 0
	curSet = set()
	while iCount <_sampleNum:
		index = random.randint(0,len(_resList)-1)
		curLine = _resList[index]
		tmp = index
		curTitleId = _resList[index].split()[0]
		if curTitleId in curSet:
			continue
		#找到起始位置.
		while tmp>0 and _resList[tmp-1].split()[0] == curTitleId:
			tmp -= 1
		#如果一个比价页只有一个商品，则跳过.
		if (tmp+1) == len(_resList) or _resList[tmp+1].split()[0] != curTitleId:
			continue
		curSet.add(curTitleId)
		iNum = 0
		fo.write(_resList[tmp])
		while iNum<_MAX_NUM and (tmp+1)<len(_resList) and _resList[tmp+1].split()[0] == curTitleId:
			tmp += 1
			iNum += 1
			fo.write(_resList[tmp])
		
		#isFirst = True #标识第一条记录
		#while iNum<_MAX_NUM and iCount<_sampleNum and (tmp+1)<len(_resList) and _resList[tmp+1].split()[0] == curTitleId:
		#	if not isFirst:
		#		fo.write(_resList[tmp])
		#	tmp += 1
		#	iNum += 1
		#	isFirst = False
		
		iCount += 1
	fo.close()

if __name__=='__main__':
	if len(sys.argv) != 3:
		#result.txt:indexPage_sorted.txt 
		print '<usage:> result.txt sample_result.txt'
		exit(1)
	print '正在从结果集中抽样...'
	getRandomSample(sys.argv[1],sys.argv[2])
	print '所抽取的样本为: ' + sys.argv[2]


