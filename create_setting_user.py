#如不存在setting_user.py则根据setting_default.py创建.否则无操作

from os import listdir

if "setting_user.py"not in listdir():
	file_setting_default=open("_src\\setting_support\\setting_default.py","r",encoding="utf-8")
	setting_default=file_setting_default.read()
	file_setting_default.close()
	file_setting_user=open("setting_user.py","w",encoding="utf-8")
	file_setting_user.write(setting_default)
	file_setting_user.close()