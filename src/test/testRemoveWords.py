#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:test fun.

import sys
import testB
sys.path.append("..")
from util import UtilFun

#测试UtilFun中的removeEnglishWords函数
def test(fileIn, fileOut):
	fi = open(fileIn, 'r')
	fo = open(fileOut, 'w')
	for line in fi:
		strTitle = UtilFun.removeEnglishWords2(line)
		fo.write(strTitle)
	fi.close()
	fo.close()

if __name__=='__main__':
	if len(sys.argv)!=3:
		print '<usage:> title.txt title_new.txt'
		exit(1)
	test(sys.argv[1],sys.argv[2])
