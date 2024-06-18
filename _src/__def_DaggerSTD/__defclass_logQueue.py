#class logQueue

class logQueue:
	"用1个定长列表构造的循环队列存储最近的若干个迭代"
	__slots__=("cap","queueList","size","full","start_idx")
	def __init__(self,cap:int=1):
		#cap	队列容量.记录最近的至多cap个迭代
		self.cap=cap
		self.queueList=[]
		self.size=0
		self.full=False
		self.start_idx=0
	def append(self,newRecord:any):
		###加入最新迭代
		#newRecord	最新迭代的值
		if self.full:
			self.queueList[self.start_idx]=newRecord
			self.start_idx=(self.start_idx+1)%self.cap
		else:
			self.queueList.append(newRecord)
			self.size+=1
			if self.size==self.cap:self.full=True
	def __getitem__(self,index:int):
		###查询日志
		###注意,对超范围序列号不报错
		#index	迭代序列号.常是负数.-1是存储中的最新迭代,-2是其前一个
		return(self.queueList[(self.start_idx+index)%self.size])