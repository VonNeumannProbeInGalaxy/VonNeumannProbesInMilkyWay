#def learnFunc

from types import FunctionType as function
def learnFunc(func:function,capL:list[int]=[16,64,256],enterScoreL:list[int]=[16,64,256],callScore:int=8):
	###改造函数使其可记录输入输出,来避免重复计算相同输入
	###被改造函数不可有遗留作用,否则会造成错误
	###达到cap时调用分数小于加入以来调用计数的cache项移入下一层cache或删去,不保证不超过cap
	#func			需改造的函数
	#capL			各层cache容量
	#enterScoreL	各层cache初始分数
	#callScore		一次调用的分数
	###in _:
	#capL			各层cache容量
	#enterScoreL	各层cache初始分数
	#cacheStage		cache层数
	#returnCache[cacheStage][arg]:
	#	[0]			返回值
	#	[1]			加入本层cache时的调用计数
	#	[2]			调用分数
	#count			调用计数
	def _(*anyArg,**anyKeyArg):
		_.count+=1
		arg=anyArg+tuple(anyKeyArg.items())
		if arg in _.returnCache[0]:_.returnCache[0][arg][2]+=callScore;notFound=False
		else:
			notFound=True
			for i in range(1,_.cacheStage):
				if arg in _.returnCache[i]:
					_.returnCache[0][arg]=[_.returnCache[i][arg][0],_.count,_.enterScoreL[0]]
					del _.returnCache[i][arg]
					notFound=False
					break
		if notFound:
			for i in range(_.cacheStage):
				if len(_.returnCache[i])>=_.capL[i]:
					toDel=[j for j in _.returnCache[i] if _.returnCache[i][j][2]<_.count-_.returnCache[i][j][1]]
					if i<_.cacheStage-1:
						for j in toDel:_.returnCache[i+1][j]=[_.returnCache[i][j][0],_.count,_.enterScoreL[i+1]]
					for j in toDel:del _.returnCache[i][j]
				else:break
			_.returnCache[0][arg]=[func(*anyArg,**anyKeyArg),_.count,_.enterScoreL[0]]
		return(_.returnCache[0][arg][0])
	_.capL=capL
	_.enterScoreL=enterScoreL
	_.cacheStage=len(capL)
	_.returnCache=[{}for i in range(_.cacheStage)]
	_.count=0
	return(_)