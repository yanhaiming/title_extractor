#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:Generate the compare index.

import sys
from util import titleUtil

_commoditySet = set()
_commodityMap = {}
STR_NOT_FOUND = "missed!"

#加载商品库信息，每一条信息对应一个唯一标识的id
def loadCommoditySet(filename):
	fi = open(filename,'r')
	id = 0
	for line in fi:
		line = line.strip()
		_commodityMap[line] = id
		id = id + 1
	print 'max_id:' + str(id)
	fi.close()


#判断两个title是否相似.
def isSimilar(strTitle1, strTitle2):
	fThreshold = 0.8
	minLen = min(len(strTitle1),len(strTitle2))
	setA = set(strTitle1)
	setB = set(strTitle2)
	setC = setA & setB
	if minLen > 0 and float(len(setC))/minLen >= fThreshold:
		return True
	else:
		return False


#传入待比价商品的信息
def genCompareIndexFile(strCommoFile,strIndexFile):
	fi = open(strCommoFile, 'r')
	fo = open(strIndexFile, 'w')
	iCount = 0 #对商品库中没有找到的商品进行计数
	for line in fi:
		strTitle = titleUtil.getTitleStr(line)
		strOriginalTitle = titleUtil.getOriginalTitleStr(line)
		if _commodityMap.has_key(strTitle):
			fo.write(str(_commodityMap[strTitle]) + "\t" + \
					strTitle + "\t" + strOriginalTitle + "\t"\
					+line.split()[1] + "\n")
			#fo.write(str(_commodityMap[strTitle]) + " " + strTitle \
			#		+ " " + line)
		else:
			isFind = False
			find_title = ''
			#for item in _commodityMap:
			#	if isSimilar(item, strTitle):
			#		find_title = item
			#		isFind = True
			#		break
			if isFind:
				fo.write(str(_commodityMap[find_title])+"\t" + \
					find_title + "\t" + strOriginalTitle + "\t"\
					+line.split()[1] + "\n")
				#fo.write(str(_commodityMap[find_title])+" " + \
				#	find_title + " " +line)
			else: 
				fo.write("-1" + STR_NOT_FOUND + " " + line)
				iCount = iCount + 1
	fi.close()
	fo.close()
	print "Total missed records: " + str(iCount)

if __name__=='__main__':
	if len(sys.argv) != 4:
		print '<usage:> seed_sorted.txt cosmetics.txt indexPage.txt'
		exit(1)
	print '正在加载商品种子库...'
	loadCommoditySet(sys.argv[1])
	print '正在生成商品比价页面索引...'
	genCompareIndexFile(sys.argv[2],sys.argv[3])

