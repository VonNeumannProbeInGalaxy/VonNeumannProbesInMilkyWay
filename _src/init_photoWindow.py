#init_photoWindow

from math					import log10,floor
from tkinter				import *
from tkinter.ttk			import *

from _src.__def_DaggerSTD.__def_closing			import *
from _src.__def_DaggerSTD.__defclass_shapePool	import *



from _src.init_starMap import *
print("mark_init_starMAP_complete")

#create window
rootWindow=Tk()
rootWindow.title(programName)
rootWindow.geometry(f"{window_width}x{window_height}+{window_placeX}+{window_placeY}")
rootWindow.resizable(False,False)
rootWindow.config(borderwidth=0,background="#3f3f3f")
exitWhenClose(rootWindow)
#create frame
mainFrame=Frame(rootWindow,width=window_width,height=window_height,borderwidth=0)
mainFrame.pack()
#create canvas
mainCanvas=Canvas(mainFrame,width=window_width,height=window_height,borderwidth=0,background=color_space)
mainCanvas.pack()
#create frameinfo
frameInfoText=mainCanvas.create_text(window_width-170,60,text="frameInfoText_here",fill=color_info,font=("Consolas",12))
#create XYline
sightCenterLineX=mainCanvas.create_line(0,window_height_div2,window_width,window_height_div2,fill=color_sightCenterXYline)
sightCenterLineY=mainCanvas.create_line(window_width_div2,0,window_width_div2,window_height,fill=color_sightCenterXYline)
mapCenterLine_pixY=window_height_div2+sightline_Y//lightYear_per_pix
mapCenterLine_pixX=window_width_div2-sightline_X//lightYear_per_pix
mapCenterLineX=mainCanvas.create_line(0,mapCenterLine_pixY,window_width,mapCenterLine_pixY,fill=color_mapCenterXYline)
mapCenterLineY=mainCanvas.create_line(mapCenterLine_pixX,0,mapCenterLine_pixX,window_height,fill=color_mapCenterXYline)
#create scale_Line&Num
scaleLevel=floor(log10(lightYear_per_pix))+3
scalelinePix=10**scaleLevel/lightYear_per_pix
scaleLine1=mainCanvas.create_line(scaleLine_pixX,scaleLine_pixY,scaleLine_pixX+scalelinePix,scaleLine_pixY,fill=color_scale)
scaleNum1=mainCanvas.create_text(scaleLine_pixX+0.5*scalelinePix,scaleLine_pixY-10,
	text=f"10**{scaleLevel} ly",fill=color_scale)
scaleLine2=mainCanvas.create_line(scaleLine_pixX,scaleLine_pixY-20,scaleLine_pixX+scalelinePix//10,scaleLine_pixY-20,fill=color_scale)
scaleNum2=mainCanvas.create_text(scaleLine_pixX+0.5*scalelinePix//10,scaleLine_pixY-30,
	text=f"10**{scaleLevel-1} ly",fill=color_scale)
scaleRate=mainCanvas.create_text(scaleLine_pixX+scalelinePix//10+70,scaleLine_pixY-30,
	text=f"{float(lightYear_per_pix):0.4}ly/pix",fill=color_scale)
#create starColorLine
if starColorLine_height:#恒星色条
	starColorLine_Tstep=9000/window_width#2000-11000K
	starColorLine_topEdge=window_height-starColorLine_height
	starColorLine=[mainCanvas.create_line(i,window_height,i,starColorLine_topEdge,
		fill=radRGB(2000+starColorLine_Tstep*i,star_fullT,star_colorT,star_gamma,star_LmapFunc,star_LmapArg,star_Lmin))
		for i in range(window_width)]
	if starColorLine_height>=20:#恒星色条关键温度标注
		starColorLine_centerY=window_height-starColorLine_height//2
		starColorLine_minT=mainCanvas.create_text(35,starColorLine_centerY,
			text="<-2000K",font="consolas",fill="#FFFFFF")
		starColorLine_maxT=mainCanvas.create_text(window_width-40,starColorLine_centerY,
			text="11000K->",font="consolas",fill="#000000")
		starColorLine_colorT=mainCanvas.create_text((star_colorT-2000)//starColorLine_Tstep,starColorLine_centerY,
			text=f"<{int(star_colorT)}K>",font="consolas",fill="#7F7F7F")
	starColorLine_scaleLine100K_height=0
	starColorLine_scaleLine1000K_height=0
	if starColorLine_height>=45:#恒星色条刻度100K+1000K
		starColorLine_scaleLine100K_height=10
		starColorLine_scaleLine1000K_height=15
	elif starColorLine_height>=35:#恒星色条刻度1000K
		starColorLine_scaleLine1000K_height=10
	if starColorLine_scaleLine100K_height:
		starColorLine_scaleLine100K=[mainCanvas.create_line(i,window_height,i,window_height-starColorLine_scaleLine100K_height,
			fill=color_starColorScale)
			for i in [i//starColorLine_Tstep for i in range(0,9001,100)]]
	if starColorLine_scaleLine1000K_height:
		starColorLine_scaleLine1000K=[mainCanvas.create_line(i,window_height,i,window_height-starColorLine_scaleLine1000K_height,
			fill=color_starColorScale,width=3)
			for i in [i//starColorLine_Tstep for i in range(0,9001,1000)]]