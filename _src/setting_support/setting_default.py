
starMapGenerator		="simple"	#选用的星图生成程序
tickTime				=1			#物理帧时间,年
TPF						=1			#每TPF物理帧刷新一次图形帧
timeLogLineCap			=1000		#时间存储队列容量.存储最近timeLogLineCap图形帧的时间
lastFrameNum			=500		#实时帧率使用最近lastFrameNum图形帧的平均.lastFrameNum<timeLogLineCap
print_frameInfo_inCMD	=True		#在cmd打印frameInfo.关闭可节省一定开销
lightYear_per_pix		=1			#图形界面每个像素边长表示的simWorld中的长度
scaleLine_pixX			=50			#较长比例尺线显示的左端坐标X
scaleLine_pixY			=60			#较长比例尺线显示的左端坐标Y
window_width			=1920		#图像宽度.适配1920x1080
window_height			=1010		#图像高度.不遮挡任务栏
window_placeX			=-8			#窗口偏移X.通常仅用于使得全屏窗口位置正确
window_placeY			=-1			#窗口偏移Y
sightline_X				=0			#视线中心位置X,相对银心,向右为正,单位光年
sightline_Y				=0			#视线中心位置Y,相对银心,向上为正,单位光年
color_info				="#FFFF00"	#信息栏
color_mapCenterXYline	="#3F7F3F"	#XY坐标轴
color_sightCenterXYline	="#003F00"	#视线XY线
color_scale				="#FFFFFF"	#比例尺线和数字
color_starColorScale	="#00BF3F"	#恒星色条刻度
color_space				="#000000"	#太空
star_fullT				=0			#恒星在屏幕上亮度饱和的表面温度
star_colorT				=6500		#恒星恰成白色的表面温度.应为屏幕色温
star_gamma				=1			#恒星显示所用的gamma值.应为屏幕gamma值
star_LmapFunc			="gamma"	#恒星显示的亮度变换方式.可选gamma,Xgamma,divLog
star_LmapArg			=10			#恒星显示的亮度变换的参数.越大越会强力地平抑恒星单位表面亮度的极端差距
star_Lmin				=0			#恒星显示的最小亮度.取[0,1]
starColorLine_height	=50			#恒星色条高度