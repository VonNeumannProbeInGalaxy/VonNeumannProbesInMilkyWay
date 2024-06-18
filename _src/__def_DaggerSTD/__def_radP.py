#def radP()

radP_c_mul_4Pi=7.12559332414319742e-07
def radP_ball(T:float,R:float,Radiance:float=1):
	###计算给定球状灰体的黑体辐射功率
	#T			温度
	#R			半径
	#Radiance	发射率
	return(Radiance*radP_c_mul_4Pi*T**4*R**2)