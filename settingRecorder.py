
from os import listdir

from _src.__def_DaggerSTD.__def_fileNameChk	import *

if "setting_user.py"not in listdir():
	print("""error:the file setting_user.py not found
	settingRecorder work based on setting_user.py
	it can NOT record setting when you have NOT special setting yourself""")
	exit()

file_setting_user=open("setting_user.py","r",encoding="utf-8")
settingStr=file_setting_user.read()
file_setting_user.close()

while True:
	recordName=input("""input:name of recordFile
	if empty,default name is NCMsettingRecord.py
>>>""")
	if not recordName:recordName="NCMsettingRecord.py"
	if fileNameChk(recordName):break
	print("error:\\/:*?\"<>| can NOT in file name")

if recordName[-3:]!=".py":recordName+=".py"
file_record=open(recordName,"w",encoding="utf-8")
file_record.write("\nfrom _src.setting_support.settingLoader import *")
file_record.write(f"\nsettingStr='''{settingStr}'''")
file_record.write("\nsettingLoader(settingStr)")
file_record.close()
print(f"""a setting record file of NCM named {recordName} has been created
you can load it again by just simply run it in the root folder of NCM""")