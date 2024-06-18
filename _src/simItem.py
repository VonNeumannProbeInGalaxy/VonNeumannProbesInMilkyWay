
from _src.__def_DaggerSTD.__defclass_logQueue	import *
from _src.__def_DaggerSTD.__def_radP			import *
from _src.__def_DaggerSTD.__def_radRGB			import *

from _src.const.const							import *
from _src.setting_support.settingSelector		import *
window_width_div2=window_width//2;window_height_div2=window_height//2



class planet:
	"岩质行星"
	__slots__=("mass","DHe3Rate","rockRate","maxSpeed_getMass","EGsp")
	def __init__(self,mass,DHe3Rate,rockRate,rho):
		self.mass				=mass				#当前质量
		self.DHe3Rate			=DHe3Rate			#含D+He3率
		self.rockRate			=rockRate			#含重元素率
		self.maxSpeed_getMass	=planet_speed_sp_getMass/rho						#从此行星开采物质的最大速率
		self.EGsp				=planet_EGsp_sp*self.mass*(rho/self.mass)**div3		#开采比能耗.E能量,G获取,sp特征

class gasGiant:
	"气态巨行星"
	__slots__=("DHe3Rate","maxSpeed_getMass","EGsp")
	def __init__(self,DHe3Rate,maxSpeed_getMass,EGsp):
		self.DHe3Rate			=DHe3Rate			#含D+He3率
		self.maxSpeed_getMass	=maxSpeed_getMass	#从此行星开采物质的最大速率
		self.EGsp				=EGsp				#比引力结合能(开采能耗).E能量,G引力,sp特征

class star:
	"恒星子系"
	__slots__=("luminosity","stellarWind","stellarWind_EKsp","DHe3Rate","rockRate","maxSpeed_getMass","EGsp","Gbattery_sp","maxP_Gbattery",
			"R","color","displayCache",
			"planetL","gasGiantL",
			"mass_HHe","massDHe3Rate","mass_rock",
			"infoLog","Estorage")
	def __init__(self,T,R,stellarWind,stellarWind_EKsp,DHe3Rate,rockRate,maxSpeed_getMass,EGsp,Gbattery_sp,maxP_Gbattery,
				planetL:list[planet],gasGiantL:list[gasGiant],
				mass_HHe:int,massDHe3Rate:int,mass_rock:int,logCap:int):
		#恒星子系总体静态参数
		self.luminosity			=radP_ball(T,R)		#光度
		self.stellarWind		=stellarWind		#星风质量流率
		self.stellarWind_EKsp	=stellarWind_EKsp	#星风比动能
		self.DHe3Rate			=DHe3Rate			#含D+He3率
		self.rockRate			=rockRate			#含重元素率
		self.maxSpeed_getMass	=maxSpeed_getMass	#举星的最大速率
		self.EGsp				=EGsp				#比引力结合能(举星比能耗).E能量,G引力,sp特征
		self.Gbattery_sp		=Gbattery_sp		#引力电池储能密度
		self.maxP_Gbattery		=maxP_Gbattery		#引力电池功率上限
		#恒星显示参数
		self.R					=R					#恒星半径/m
		self.color				=radRGB(T,star_fullT,star_colorT,star_gamma,star_LmapFunc,star_LmapArg,star_Lmin)#恒星颜色
		self.displayCache={							#恒星显示缓存
			"place_pixX"		:0,					#相对恒星系中心的像素偏移X
			"place_pixY"		:0,					#相对恒星系中心的像素偏移Y
			"R_pix"				:1,					#像素半径的向下取整值
			"outline"			:"#000000",			#边缘颜色,用于显示半像素
		}
		#恒星子系内容
		self.planetL			=planetL			#岩质行星列表
		self.gasGiantL			=gasGiantL			#气态巨行星列表
		self.mass_HHe			=mass_HHe			#零散小天体H+He质量
		self.massDHe3Rate		=massDHe3Rate		#零散小天体H+He中D+He3质量比例
		self.mass_rock			=mass_rock			#零散小天体岩质质量
		self.infoLog			=logQueue(logCap)	#自身的信息日志队列
		self.infoLog.append({
			"mass_dysonSwarm"	:0,					#戴森云质量
			"mass_Gbattery"		:0,					#引力电池质量(HHe4库存量)
			"mass_factory"		:0,					#工厂质量.包括星风卫星,物质开采器,举星器,飞轮电池,核反应堆,戴森光束
		})
		self.Estorage			=0					#引力电池的当前储能(无法快速放能,快速放能需要飞轮电池中转)

class starSYS:
	"恒星系"
	__slots__=("x","y","z","distanceL","displayCache","starL","infoLog","actionL","DHe3store")
	def __init__(self,x,y,z,starL:list[star],logCap:int):
		self.x,self.y,self.z	=x,y,z				#恒星系坐标
		self.distanceL			=[]					#与其它恒星系的距离列表,单位:光帧(光速*物理帧时间)
		self.displayCache={							#恒星系显示缓存
			"backTeamColorR"	:0					#背景队伍识别色块半径
		}
		self.starL				=starL				#恒星子系列表
		self.infoLog			=logQueue(logCap)	#自身的信息日志队列
		self.infoLog.append({
			"teamID"			:None,				#当前占领方的队伍编号
			"controller"		:None,				#ASI占领者对象
			"eventL_open"		:[],				#公开事件列表
			"eventL_team"		:[],				#队内事件列表
		})
		self.actionL			=[]					#系内事件列表
		self.DHe3store			=0					#DHe3库存量