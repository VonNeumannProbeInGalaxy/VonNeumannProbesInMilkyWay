#def uncMatTab()

def uncMatTab(strMat:list[list[str]],tabWidth:int=4):
	###用tab行列对齐地输出unicode字符串矩阵
	###允许各行字符串数不同
	###成员字符串不可含有ascii控制符
	#strMat		给定字符串矩阵
	#tabWidth	Tab宽度
	L=len(strMat);countL=[len(i)for i in strMat];countLsub1=[i-1 for i in countL]
	lenMat=[[(len(j)+sum([(ord(k)>=128)for k in j]))for j in i]for i in strMat]
	wideL=[max(lenMat[j][i]for j in range(L)if(countL[j]>i))//tabWidth+1 for i in range(max(countL))]
	return("".join([strMat[i][j]+("\n"if(j==countLsub1[i])else("\t"*(wideL[j]-lenMat[i][j]//tabWidth)))for i in range(L)for j in range(countL[i])])[:-1])