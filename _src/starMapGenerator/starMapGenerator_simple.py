
from _src.simItem	import *

#other_import
pass

#starMapGenerator_setting
starSYSnum=1000	#恒星系数目
starMapR=1000	#恒星系分布区域最远两点距离的一半.单位:光年

starMap:list[starSYS]=[]
#add_starSYS
for i in range(starSYSnum):pass#needRecoding
#add_distanceL
for i in starMap:i.distanceL=[((i.x-j.x)**2+(i.y-j.y)**2+(i.z-j.z)**2)**0.5//tickTime+1 for j in starMap]