#用于自动恢复至初始状态

from os		import chdir,listdir,remove
from shutil	import rmtree

dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")
if "NCMsettingRecord.py"in dir:remove("NCMsettingRecord.py")
if "setting_user.py"	in dir:remove("setting_user.py")

chdir("_src")
dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")

chdir("__def_DaggerSTD")
dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")
chdir("..")

chdir("starMapGenerator")
dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")
chdir("..")

chdir("const")
dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")
chdir("..")

chdir("setting_support")
dir=listdir()
if "__pycache__"		in dir:rmtree("__pycache__")

file_settingSelector=open("settingSelector.py","w",encoding="utf-8")
file_settingSelector.write("""
from _src.setting_support.setting_default	import *

from create_setting_user					import *

f_self=open("_src\\setting_support\\settingSelector.py","w",encoding="utf-8")
f_self.write("\\nfrom setting_user import *")
f_self.close()""")
file_settingSelector.close()