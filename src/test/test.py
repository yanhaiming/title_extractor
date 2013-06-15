import sys
import testB
sys.path.append("..")
from util import UtilFun

def fun1(str):
	print str
	str = str + "aaa"
	return str

def fun2():
	str = "bbb"
	print 'before:'+str
	str = fun1(str)
	print 'after:'+str

def testGetOriginalTitle(fileIn,fileOut):
	fi = open(filename,'r')
	for line in fi:
		print line

if __name__=='__main__':
	UtilFun.sayHello("aa")
