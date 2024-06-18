
#const
from math import pi as Pi
Pi_mul4div3	=Pi*4/3
div3		=1/3
G			=6.6742e-11		#引力常数
radP_c		=5.670367e-8	#W/m**2/K**4.斯特藩-玻耳兹曼常数
#var
radT		=1145			#K.地表散热温度
eta_launch	=0.4			#发射效率

#岩质行星开采物质流率-密度的积常数
planet_speed_sp_getMass=2*eta_launch/(1-eta_launch)*radP_c*radT**4/2/G*3
#岩质行星开采比能耗的常数部分
planet_EGsp_sp=G*Pi_mul4div3**div3/eta_launch

if __name__=="__main__":
	print(f"{planet_speed_sp_getMass=:e}")
	print(f"{planet_EGsp_sp=:e}")