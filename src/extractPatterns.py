#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:Using seed.txt to find new titles.

import sys
import re

_setSeed = set()
_dictPattern = {}



#加载商品种子库信息.
def loadSeed(seedFileName):
	print '开始从'+seedFileName+'中加载种子库信息.'
	fi = open(seedFileName,'r')

	for line in fi:
		strTitle = line.strip('\n')
		_setSeed.add(strTitle)
	
	fi.close()

#从一个商品的信息中发现模板pattern,若发现，则加入到模板词典中.
#strLinePurged:经过处理的一行商品信息.
#strTitleName:种子库中的商品信息.
#若能生成Pattern，则返回True；否则返回False.
def getPattern(strLinePurged,strTitleName):
	#找到子串，则可以生产一个模板.
	strLinePurged = strLinePurged.strip('\n')
	if strLinePurged.find(strTitleName) != -1 and len(strLinePurged)!=len(strTitleName):
		strPattern = strLinePurged.replace(strTitleName,'.*')
		if _dictPattern.has_key(strPattern):
			_dictPattern[strPattern] += 1
		else:
			_dictPattern[strPattern] = 1
		return True
	else:
		return False
	
#通过种子库文件，在新的商品信息中去寻找商品名模板，
#处理完后形成一个新的模板文件.
#f_line_purged:去除掉url等前缀信息的商品信息.
#f_seed:准确率较高的种子库
#f_pattern_found通过种子所发现的模板
def extract_patterns(f_line_purged, f_seed, f_pattern_found):
	loadSeed(f_seed)
	print '寻找新的商品名...'
	fi_line = open(f_line_purged,'r')
	fo_pattern = open(f_pattern_found,'w')

	#首先生成一个模板库
	print '生成模板库...'
	for line in fi_line:
		for title in _setSeed:
			getPattern(line, title)
	for pattern in _dictPattern:
		if _dictPattern[pattern] > 5:
			print 'pattern=' + pattern + ', count = ' + str(_dictPattern[pattern])
			fo_pattern.write(pattern+'\n')
	
	
	fi_line.close()
	fo_pattern.close()



if __name__ == '__main__':
	if len(sys.argv) != 4:
		print '<usage:> line_purged.txt seed.txt pattern_found.txt'
		exit(1)
	extract_patterns(sys.argv[1],sys.argv[2],sys.argv[3])
