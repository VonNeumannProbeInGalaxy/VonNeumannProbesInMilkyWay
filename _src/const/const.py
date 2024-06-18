
#special
programName="VonNeumannProbes_haveChickenDinner_inMilkyWay-v0.8.5.37.20240321"
from _src.const.importStage import *
veryShortTime=1e-6#1us.be used to replace 0.0s time,so can solve div0_error

#math
from math import pi as Pi
Pi_mul4div3=Pi*4/3
div3=1/3

#physics
G=6.67408e-11	#引力常数

#engineering
from _src.const.planet_sp	import planet_speed_sp_getMass	#岩质行星开采物质流率-密度的积常数
from _src.const.planet_sp	import planet_EGsp_sp			#岩质行星开采比能耗的常数部分