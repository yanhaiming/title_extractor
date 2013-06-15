#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:some useful functions.

import sys
import re

_strSplit = ">"
_MIN_TITLE_LEN = 20
_MAX_TITLE_LEN = 80

#删除title中一些干扰字符.
def removeCharSetInStr(str):
	strRet = str.strip()
	strRet = strRet.upper()
	charList = ['2011','2012','2013','.','/','\\','[',']','）',\
			'（','【','】','(',')','，','+','-',\
			'\'','‘','’','100%','德国原装进口',\
			'年','&','#','德国','当当自营','国内发货','“',\
			'”','1212心动价','年中大促','·','／','女人我最大推荐',
			'°','《','》','其他','!','．．','Λ','＇','',\
			'＆','－','［嗳呵旗舰店］','"','"','金蛇迎春满赠促销',\
			'金蛇迎春满就送','．．','金蛇迎春全民满减','>','<',\
			'@','','','']
	for item in charList:
		strRet = strRet.replace(item,'')
	return strRet

#判断title中是否有化妆品容量信息
def isHasVolumeData(strTitle):
	strTitle = strTitle.upper()
	match = re.search(r'\d+(ML|毫升)',strTitle)
	if not match:
		return False
	else:
		return True

#判断title中是否有化妆品重量量信息
def isHasWeightData(strTitle):
	strTitle = strTitle.upper()
	match = re.search(r'\d+(G|克)',strTitle)
	if not match:
		return False
	else:
		return True

#判断title中是否有化妆品容量信息
def getVolumeData(strTitle):
	strTitle = strTitle.upper()
	match = re.search(r'\d+(ML|毫升)',strTitle)
	if not match:
		return None
	else:
		return match.group().title()

#判断title中是否有化妆品重量量信息
def getWeightData(strTitle):
	strTitle = strTitle.upper()
	match = re.search(r'\d+(G|克)',strTitle)
	if not match:
		return None
	else:
		return match.group().title()
#利用正则表达式删除一些无效字符，如7折！
def removeNoiseStr(strTitle):
	strRet = ""
	strRet = re.sub('\w折！','',strTitle)
	strRet = re.sub('您当前的位置.*','',strRet)
	strRet = re.sub('首页.*','',strRet)
	return strRet

#删除一个title中的英文字符，其中数字+ML(毫升)和数字+G(克)这两种字符不会被删除.
#strTitle：经过处理后的title.
def removeEnglishWords(strTitle):
	#print "strTitle:" + strTitle
	strList = list(strTitle)
	iLen = len(strList)
	for i in range(0,iLen):
		ch = strList[i]
		if ch == 'G' and (i-1)>=0 and strList[i-1]>='0' and strList[i-1]<='9':
			continue
		elif ch == 'M' and (i+1)<iLen and \
				strList[i+1]=='L' and (i-1)>=0 \
				and strList[i-1]>='0' and \
				strList[i-1] <='9':
					continue
		elif ch == 'L' and (i-1)>=0 and strList[i-1]=='M':
			continue
		elif ch >= 'A' and ch <='Z':
			strList[i] = ''
	strRet = ''.join(strList)
	#print 'strRet:' + strRet
	return strRet

#将title前面的url和时间戳信息去掉.
def removeTitlePre(strLine):
	strRet = ""
	strList = strLine.split()[4:]
	strRet = '\t'.join(strList)
	return strRet

#从一条商品记录中获取经过处理后的title信息.
def getTitleStr(strLineWithPre):
	strLine = removeTitlePre(strLineWithPre)
	#将所有英文字符都转换成大写的。
	strLine = strLine.upper()
	#先从一条记录的中间部分去抽取title.
	iEndT = strLine.find(_strSplit)
	strTemp = strLine[0:iEndT]
	strTitle = ""
	
	#print 'aa'+strTemp

	#当所找到的title过于短时,从一条记录的层次分类信息的
	#最后一项去抽取title.
	if len(strTemp.strip())<_MIN_TITLE_LEN:
		strTemp = strLine[strLine.rfind(_strSplit):len(strLine)]
		strList = strTemp.split()
		for i in range(0,len(strList)):
			strTitle += strList[i]
	else:
		strList = strTemp.split()
		for i in range(0,len(strList)-1): 
			if len(strTitle)>=_MAX_TITLE_LEN:
				break;
			strTitle += strList[i]
	strTitle = removeCharSetInStr(strTitle)
	
	#判断处理后的strTitle中是否含有容量信息，如果
	#原来的strLine中有，那么就将这个信息加进来.
	#if not isHasVolumeData(strTitle):
	#	strVolume = getVolumeData(strLine)
	#	if strVolume:
	#		strTitle += strVolume
			#print strVolume
	#if not isHasWeightData(strTitle):
	#	strWeight = getWeightData(strLine)
	#	if strWeight:
	#		strTitle += strWeight
			#print strWeight
	#删除英文字符，消除品牌的二义性.
	strTitle = removeEnglishWords(strTitle)
	strTitle = removeNoiseStr(strTitle)
	#print 'strTitle: ' + strTitle
	return strTitle

#从一条商品记录中获取未经处理的title信息，即去掉前面的
#URL、时间戳等信息
def getOriginalTitleStr(strLine):
	strRet = ""
	iBegin = 4
	strList = strLine.split()
	iBegin = strLine.find(strList[4])#找到title开始的地方.
	strRet = strLine[iBegin:]
	iEnd = len(strRet)-1
	strRet = strRet[0:iEnd]#去除换行符.
	#for i in range(4,len(strList)):
	#	strRet += strList[i]
	return strRet

def sayHello(str):
	print "hello"+str
