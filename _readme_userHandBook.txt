welcome to NCM=Von<N>eumannProbes_have<C>hickenDinner_in<M>ilkyWay

===basic===

---how to run---
just run file NCM.py in folder root

---how to setting---
just change value of settingKey in file setting_user.py in folder root
tip:setting_user.py will be auto-created after run NCM for first time,
	or you can just run create_setting_user.py in folder root

---how to clear---
just run file tool_delCache.py in folder root
if you always use NCM in good way,and never change file in wrong way
it could promising reset NCM to initial state

---how to sync setting to new virsion---
step1:record setting
	run file settingRecorder.py in folder root
	it will create a setting record file of NCM,whose default name is NCMsettingRecord.py
	you can find it in folder root
	tip:you must have yourself setting_user.py to record setting,
		because record default setting is meaningless
step2:save setting record file
	save setting record file you got in step1 by yourself
step3:load setting
	copy setting record file need to load into folder root of new virsion of NCM
	then just run it
	if everything is good,it is OK now
	if something wrong,it may means:
		-case1:new virsion have different settingKey
			some old settingKey may have been delelted
		-case2:new virsion have different way to load setting
			so it need a few changing of setting record file
		-case3:setting record file try to load is bad
	anyway,you should check setting after loading

===extend===

---what has been changed in new virsion---
view file updateLog.txt in folder root

---how file link to each other---
view file importStage.py in folder const in folder _src

---how to send idea of improvement---
view NBP0 in folder NBP

---how can I make myself starMapGenerator---
step1:coding starMapGenerator
	code a .py file with starMapGenerator-standard
step2:add your file
	copy your starMapGenerator file into folder starMapGenerator in folder _src
step3:loading
	change file init_starMap in folder _src
	you will know how to do it.just follow example
step4:choose it
	select your starMapGenerator by changing settingKey starMapGenerator
	it is OK now