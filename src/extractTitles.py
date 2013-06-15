#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:Using seed.txt to find new titles.

import re
import sys

_patternList = []
_setSeed = set()

#加载商品种子库信息.
def loadSeed(seedFileName):
	print '开始从'+seedFileName+'中加载种子库信息.'
	fi = open(seedFileName,'r')

	for line in fi:
		strTitle = line.strip('\n')
		_setSeed.add(strTitle)
	
	fi.close()

#从模板文件中加载模板
def loadPatterns(patternFileName):
    print '加载模板...'
    fi = open(patternFileName)

    for line in fi:
        strPattern = line.strip('\n')
        _patternList.append(strPattern)

    fi.close()

#给定一个模板strPattern，从新的商品信息中抽取新的title信息.
#strLine:包含title信息的字符串，可能含有其他干扰字符，如"五一特价"、"港或直通"等
#strPattern: 利用种子所发现的模板信息.
#如strLine为:ab123cd, strPattern为ab.*cd则返回123.
#如果抽取成功则返回title名称，否则返回None。
def getTitle(strLine, strPattern):
    match = re.search(strPattern,strLine)
    if match:
        index = strPattern.find('.*')
        prefix = strPattern[0:index]
        suffix = strPattern[index+2:]
        strTitle = strLine.replace(prefix,'').replace(suffix,'')
        strTitle = strTitle.strip('\n')
        return strTitle
    else:
        return None

def saveTitleToFile(f_out_new_seed):
	fo_new_seed = open(f_out_new_seed,'w')
	for title in _setSeed:
		fo_new_seed.write(title+'\n')
	
	fo_new_seed.close()
#给定一个种子库和模板，发现新的商品title，并将新的商品title与种子库合并生成一个
#新的更大的种子库
#f_in_seed:种子库
#f_in_pattern: 模板文件（利用种子库发现的）
#f_in_cosmetics: 新的化妆品数据.
#f_out_new_seed:输出一个更大的种子库
def extractTitles(f_in_seed,f_in_pattern,f_in_cosmetics,f_out_new_seed):
    loadSeed(f_in_seed)
    loadPatterns(f_in_pattern)
    fi_cosmetics = open(f_in_cosmetics,'r')
	
    for line in fi_cosmetics:
		for pattern in _patternList:
			title = getTitle(line,pattern)
			if title and title not in _setSeed:
				print 'find new title:'+title
				_setSeed.add(title)
    saveTitleToFile(f_out_new_seed)
    fi_cosmetics.close()



if __name__ == '__main__':
	if len(sys.argv) != 5:
		print '<usage:> f_in_seed f_in_pattern f_in_cosmetics f_out_new_seed'
		exit(1)
	extractTitles(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
