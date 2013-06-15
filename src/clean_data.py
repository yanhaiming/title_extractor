#!/usr/local/bin/python
#encoding: gbk
#author: yanhaiming@baidu.com
#brief:清洗数据

import sys

#待匹配的噪声字符
strNoiseList = ['图书','真丝围巾']

#判断某一行数据是否为噪声数据
def isNoiseData(strLine):
	for item in strNoisList:
		if strLine.find(item) != -1:
			return True
	return False


#清洗数据，将不属于化妆品的记录去除，如"图书"、"真丝围巾"等。
#fileIn:清洗前的数据.
#fileOut:清洗后的数据
def purge_data(fileIn,fileOut):
	print '开始清洗数据...'
	fi = open(fileIn,'r')
	fo = open(fileOut,'w')
	fo_noise = open('noise.txt','w')
	for line in fileIn:
		if not isNoiseData(line):
			fo.write(line)
		else:
			fo_noise.write(line)

	fi.close()
	fo.close()
	fo_noise.close()
	print '清洗完成...'


if __name__=='__main__':
	if len(sys.argv) != 3:
		print '<usage:> cosmetics.txt cosmetics_purged.txt'
		exit(1)
	purge_data(sys.argv[1],sys.argv[2])

