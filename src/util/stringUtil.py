#!/usr/local/bin/python
#encoding: utf-8
#author: yanhaiming@baidu.com
#brief:string util.

import codecs
import string
import re

convertGB18030 = codecs.lookup("gb18030")
convertUTF8 = codecs.lookup("utf8")

def gb2uni(strLine):
	    strUniLine = convertGB18030.decode(strLine)[0]
		    return strUniLine
		
def utf82uni(strLine):
	strUniLine = convertUTF8.decode(strLine)[0]
	return strUniLine

def uni2gb(strLine):
	strGBLine = convertGB18030.encode(strLine)[0]
	return strGBLine

def uni2utf8(strLine):
	strUTF8Line = convertUTF8.encode(strLine)[0]
	return strUTF8Line
