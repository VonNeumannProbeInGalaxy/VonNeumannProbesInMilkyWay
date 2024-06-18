#def fileNameChk()

notFileName="\\/:*?\"<>|"
def fileNameChk(name:str):
	###判断所给字符串是否可用作文件名
	#name	所给字符串
	if not name:return(False)
	for i in notFileName:
		if i in name:return(False)
	return(True)