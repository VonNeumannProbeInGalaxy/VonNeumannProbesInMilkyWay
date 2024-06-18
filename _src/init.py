#init_all

from time	import time

#run
print("mark_init_start")

#init_starMap is in init_photoWindow

from _src.init_photoWindow import *
print("mark_init_photoWindow_complete")

#prepareForMainloop
timeLog=logQueue(timeLogLineCap)
timeLog.append((startTime:=time()))
frameCount=0
print("mark_sim_start")
if print_frameInfo_inCMD:print("\n"*6)#为在cmd中打印的frame_info预留空间