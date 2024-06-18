#NCM means Von<N>eumannProbes_have<C>hickenDinner_in<M>ilkyWay

from _src.init		import *
from _src.tickGo	import *



#toolFunc
def lastFPS():
	#最近lastFrameNum图形帧的平均图形帧率
	"""tip:
	lastTPS=lastFPS*TPF
	lastTimeRate=lastTPS*tickTime
	"""
	if frameCount>=lastFrameNum:return(lastFrameNum/(timeLog[-1]-timeLog[-1-lastFrameNum]))
	else:return(frameCount/(deltaTime if(deltaTime:=timeLog[-1]-timeLog[0])else veryShortTime))
def FPSinfo():
	return(f"""
===the {frameCount}th photoFrame info===
realTime used: {(totalTime:=timeLog[-1]-startTime):18.2f}s
simTime passed:{(totalSimTime:=frameCount*TPF*tickTime):18.1f}year
last {lastFrameNum} frame / general:
{(thisFPS:=lastFPS()):14.3f} /{(generalFPS:=frameCount/(totalTime if totalTime else veryShortTime)):14.3f} FPS
{(thisTPS:=thisFPS*TPF):14.2f} /{(generalTPS:=generalFPS*TPF):14.2f} TPS
{thisTPS*tickTime:14.1f} /{generalTPS*tickTime:14.1f} year/s""")



def photoRefresh():
	#图形帧刷新程序
	#refresh frameInfo
	_=FPSinfo()
	if print_frameInfo_inCMD:print("\x1B[8F"+_)
	mainCanvas.itemconfig(frameInfoText,text=_)
	#redraw
	pass
	#update
	mainCanvas.update()
	mainFrame.update()
	rootWindow.update()



while True:
	#物理帧
	for i in range(TPF):tickGo(tickTime)
	#图形帧
	timeLog.append(time())
	frameCount+=1
	photoRefresh()
#run_end

rootWindow.mainloop()