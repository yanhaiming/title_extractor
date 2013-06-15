
import sys
import testB
sys.path.append("..")
from util import titleUtil

def getTitle(cosFileName,outFile):
	print 'testing the function getTitleStr in UtilFun.py'
	fi = open(cosFileName,'r')
	fo = open(outFile,'w')
	for line in fi:
		strTitle = titleUtil.getTitleStr(line)
		fo.write(strTitle+"\n")
	fi.close()
	fo.close()


if __name__=='__main__':
	if len(sys.argv)!=3:
		print '<usage>: costetics.txt title_test.txt'
		exit(1)
	getTitle(sys.argv[1],sys.argv[2])
