
from _src.setting_support.settingLoader import *
settingStr='''
star_fullT				=11000		#恒星在屏幕上亮度饱和的表面温度
star_colorT				=6500		#恒星恰成白色的表面温度.应为屏幕色温
star_gamma				=2.2		#恒星显示所用的gamma值.应为屏幕gamma值
star_LmapFunc			="gamma"	#恒星显示的亮度变换方式.可选gamma,Xgamma,divLog
star_LmapArg			=10			#恒星显示的亮度变换的参数.越大越会强力地平抑恒星单位表面亮度的极端差距
star_Lmin				=0			#恒星显示的最小亮度.取[0,1]'''
settingLoader(settingStr)