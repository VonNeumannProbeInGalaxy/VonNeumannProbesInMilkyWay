#def radRGB()

#fast_with_aFewError
from math import exp,log
c2_div_STDcolorR=2.05539304255011812e+04
c2_div_STDcolorG=2.63463675111716257e+04
c2_div_STDcolorB=3.30145738821726118e+04
hexFF			=2.55999999999999943e+02#256-1/(1<<44)
STD_T_D65		=6500		#D65标准色温
STDgamma		=2.2		#标准gamma值
LmapFunc_gamma	="gamma"
LmapFunc_Xgamma	="Xgamma"
LmapFunc_divLog	="divLog"
def radRGB(T:float,fullT:float=0,colorT:float=STD_T_D65,gamma:float=STDgamma,LmapFunc:str=LmapFunc_gamma,LmapArg:float=None,Lmin:float=0):
	###计算给定条件下给定温度黑体辐射的原彩RGB感官值
	#T			黑体温度.>=14K否则浮点溢出
	#fullT		RGB分量饱和温度.设为None使白光饱和
	#colorT		白光色温
	#gamma		伽马值
	#LmapFunc	亮度映射方式.[0,1]>>>[0,1].保持RGB比例.可选gamma,Xgamma,divLog
	#LmapArg	亮度映射参数
	#Lmin		最小亮度.[0,1]>>>[Lmin,1]保持RGB比例线性映射
	fullT=max(T,(fullT if fullT!=None else colorT))
	_=(fullT-colorT)/(colorT*fullT*gamma)
	R=exp(c2_div_STDcolorR*_)
	G=exp(c2_div_STDcolorG*_)
	B=exp(c2_div_STDcolorB*_)
	LmulRate=1/max(R,G,B)
	if T<fullT:
		_=(T-fullT)/(fullT*T*gamma)
		R*=exp(c2_div_STDcolorR*_)
		G*=exp(c2_div_STDcolorG*_)
		B*=exp(c2_div_STDcolorB*_)
		maxRGB=max(R,G,B)*LmulRate
		if LmapArg:
			LmapRate=(maxRGB*2-maxRGB**2)**(1/LmapArg)/maxRGB	if LmapFunc=="Xgamma"\
				else 1/((1-log(maxRGB)/LmapArg)*maxRGB)			if LmapFunc=="divLog"\
				else maxRGB**(1/LmapArg-1)						#if LmapFunc=="gamma"
			LmulRate*=LmapRate
			maxRGB*=LmapRate
		if Lmin:LmulRate*=1+Lmin*(1/maxRGB-1)
	LmulRate*=hexFF
	R*=LmulRate
	G*=LmulRate
	B*=LmulRate
	return(f"#{int(R):02X}{int(G):02X}{int(B):02X}")



if __name__=="__main__":
	from tkinter import *
	rootWindow=Tk()
	rootWindow.title("test_#_def_radRGB.py")
	rootWindow.geometry(f"1000x500+-8+-1")
	mainFrame=Frame(rootWindow,width=1000,height=500,background="#000000",borderwidth=0);mainFrame.pack()
	mainCanvas=Canvas(mainFrame,width=1000,height=500,background="#000000",borderwidth=0);mainCanvas.pack()

	for i in range(10,1100,10):mainCanvas.create_line(i,0,i,500,fill="#3F3F3F")#整100K线
	for i in range(100,1100,100):mainCanvas.create_line(i,0,i,500,fill="#7F7F7F")#整1000K线
	mainCanvas.create_line(550,0,550,500,fill="#FFFFFF")#6500K线

	TL=1000				#温度下限
	TH=11000			#温度上限
	Tstep=(TH-TL)/1000	#温度组距
	for i in range(1000):
		mainCanvas.create_line(i,10,i,90,fill=(_:=radRGB(TL+Tstep*i)))
		if _=="#FFFFFF":mainCanvas.create_line(i,10,i,30,fill="#000000");print(i)
		mainCanvas.create_line(i,100,i,140,fill=radRGB(TL+Tstep*i,None))
		mainCanvas.create_line(i,150,i,190,fill=radRGB(TL+Tstep*i,TH))
		mainCanvas.create_line(i,200,i,240,fill=radRGB(TL+Tstep*i,gamma=1))
		mainCanvas.create_line(i,250,i,290,fill=radRGB(TL+Tstep*i,gamma=0.5))
		mainCanvas.create_line(i,300,i,340,fill=radRGB(TL+Tstep*i,TH,LmapArg=10))
		mainCanvas.create_line(i,350,i,390,fill=radRGB(TL+Tstep*i,TH,gamma=1,LmapArg=22))
		mainCanvas.create_line(i,400,i,440,fill=radRGB(TL+Tstep*i,TH,LmapFunc="Xgamma",LmapArg=10))
		mainCanvas.create_line(i,450,i,490,fill=radRGB(TL+Tstep*i,TH,LmapFunc="divLog",LmapArg=10))

	mainCanvas.create_text(50,50,text="<- 1000K",font="consolas",fill="#FFFFFF")
	mainCanvas.create_text(950,50,text="11000K ->",font="consolas",fill="#000000")
	mainCanvas.create_text(550,50,text="<6500K>",font="consolas",fill="#7F7F7F")

	mainCanvas.update()
	mainFrame.update()
	rootWindow.update()
	rootWindow.mainloop()