#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:make seed commodity dict.

import sys
import re
from util import titleUtil

iMaxBreedSize = 70
strSeedCommodityFileName = "seed.txt"
commoditySet = set()
_minTitleLen = 20

#生成种子词典,输入：化妆品数据文件，生成的种子商品库文件.
def mkSeedCommDict(cosFileName,seedFileName):
	print '正在生成种子商品库...'

	fi = open(cosFileName, 'r')
	fo = open(seedFileName, 'w')

	for line in fi:
		strTitle = titleUtil.getTitleStr(line)
		#将长度过小的非法title过滤.
		if len(strTitle) >= _minTitleLen:
			commoditySet.add(strTitle)

	for item in commoditySet:
		fo.write(item+'\n')

	fi.close()
	fo.close()


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print '<usage:> cosmetics.txt seed.txt'
		exit(1)
	mkSeedCommDict(sys.argv[1],sys.argv[2])
