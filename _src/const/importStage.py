#this file show import relationship of file in ASCII-photo
																																			#tab
importStage="""
NCM-+-init------+-init_photoWindow--+-__def_closing
	|								+-__defclass_shapePool
	|								+-init_starMap----------+-starMapGenerator_chosen---+-simItem$
	+-tickGO

$simItem----+-__defclass_logQueue
			+-__def_radP
			+-__def_radRGB
			+-const-----------------+-importStage
			|						+-[otherConstFile]
			+-settingSelector$
	
$settingSelector----+--------------+seting_default
					+<setting_user>+*create_setting_user

NCMsettingRecord----+<<settingRecorder(setting_user)----__def_fileNameChk
					+settingLoader--*create_setting_user
									+-__def_ACKnormal.py
									+-__def_uncMatTab.py

example:
-typeA
child1--+-parent1
child2--+-parent2
-typeB
child---singleParent
-typeC
child---+-------------+default
		+<change-able>+*tool
-typeD
child---<<fileCreater(sourceFile)
-typeE
user----*tool
-typeF
child---output$
$output-parent
""".expandtabs(4)