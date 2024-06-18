
from _src.setting_support.settingSelector	import *

from _src.__def_DaggerSTD.__def_ACKnormal	import *
from _src.__def_DaggerSTD.__def_uncMatTab	import *

def settingLoader(settingStr:str):
	existFailure=False
	#setting_record
	settingL=[line.split(maxsplit=2) for line in settingStr.split("\n") if line]
	#setting_now
	file_setting_user=open("setting_user.py","r",encoding="utf-8")
	settingL_now=[line.split(maxsplit=2) for line in file_setting_user.read().split("\n") if line]
	file_setting_user.close()
	#add setting
	addKeyL=[i[0] for i in settingL]
	nowKeyL=[i[0] for i in settingL_now]
	for i in range(len(addKeyL)):
		if (addKey:=addKeyL[i]) in nowKeyL:
			settingL_now[nowKeyL.index(addKey)][1:len(settingL[i])]=settingL[i][1:]
			print(f"load setting successful:{settingL[i][0]}{settingL[i][1]}")
		else:print(f"load setting failed:setting key {addKey} NOT found");existFailure=True
	#ACK if existFailure
	if existFailure:
		print("""There are some setting load failed
it may mean exist difference between virsion,or setting record file bad.you should check it later anyway
do you want to write down setting which successfully loaded?
if cancel,NO anything will be changed""")
		if (not ACKnormal("en")):print("have canceled setting Loading.no any setting been changed");return
	#write down into setting_user.py
	file_setting_user=open("setting_user.py","w",encoding="utf-8")
	file_setting_user.write("\n"+uncMatTab(settingL_now))
	file_setting_user.close()
	print("all successfully loaded setting have been write down into setting_user.py")