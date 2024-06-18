#class shapePool

from tkinter	import Canvas
from types		import FunctionType as function

class shapePool:
	"图形池"
	###用于统一分配频繁变动的同一类图形的显示任务,来节省显示开销
	__slots__=("canvas","createFunc","freeNum","freeRate","freeArg","freeKeyArg",
			   "poolList","size","index_now","index_free")
	def __init__(self,canvas:Canvas,createFunc:function,freeNum:int,freeRate:float,*freeArg,**freeKeyArg):
		#canvas			从属的Canvas对象
		#createFunc		新建该类图形所用的构造函数,即canvas.create_anyShape()
		#freeNum		不删除数量不超过freeNum的空余图形
		#freeRate		不删除数量不超过已用图形的freeRate倍的空余图形
		#*freeArg		一组使该类图形保持在显示范围外的参数,位置参数部分
		#**freeKeyArg	一组使该类图形保持在显示范围外的参数,关键字参数部分
		self.canvas		=canvas
		self.createFunc	=createFunc
		self.freeNum	=freeNum
		self.freeRate	=freeRate
		self.freeArg	=freeArg
		self.freeKeyArg	=freeKeyArg
		self.poolList	=[]
		self.size		=0
		self.index_now	=0
		self.index_free	=0
	def draw(self,*otherArg,**otherKeyArg):
		###分配一个图形的绘制任务
		###每图形帧需重分配
		if self.index_now<self.size:#池中图形数量充足
			thisShape=self.poolList[self.index_now]
			self.canvas.coords(thisShape,otherArg)
			self.canvas.itemconfig(thisShape,otherKeyArg)
		else:#池中图形数量不足,需新建
			self.poolList.append(self.createFunc(otherArg,otherKeyArg))
			self.size+=1
		self.index_now+=1
	def	endFrame(self):
		###结束一个图形帧
		#删除过多的空闲图形
		index_tooFree=self.index_now+max(int(self.index_now*self.freeRate)+1,self.freeNum)
		for i in self.poolList[index_tooFree:]:self.canvas.delete(i)
		self.poolList=self.poolList[:index_tooFree];self.size=len(self.poolList)
		#令保留的空闲图形保持在显示范围外
		for i in self.poolList[self.index_now:self.index_free]:
			self.canvas.coords(i,self.freeArg)
			self.canvas.itemconfig(i,self.freeKeyArg)
		#init modeArg
		self.index_free=self.index_now
		self.index_now=0