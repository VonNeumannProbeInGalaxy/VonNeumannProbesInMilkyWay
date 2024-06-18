#init_starMAP

from _src.setting_support.settingSelector import starMapGenerator

if starMapGenerator=="example":
	from _src.starMapGenerator.starMapGeneratorExample import *
if starMapGenerator=="simple":
	from _src.starMapGenerator.starMapGenerator_simple import *
#add yourself starMapGenerator here