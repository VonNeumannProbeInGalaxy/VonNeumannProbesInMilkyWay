#def ACKnormal()

zh={"ask"	:"输入Y确认,quit取消\n>>>",
	"reAsk"	:"错误-请确认或取消",
	"apply"	:"提示-已应用操作",
	"cancel":"提示-已取消操作",
}
en={"ask"	:"Enter <Y> to check,or <quit> to cancel\n>>>",
	"reAsk"	:"Error-either check or cancel",
	"apply"	:"Tip-work has applied",
	"cancel":"Tip-work has canceled",
}
langList={"en":en,"zh":zh,}
def ACKnormal(lang="zh"):
	###用于用户确认操作.输入Y确认,quit取消.其它重试
	#lang	提示所用语言.无所选语言则使用英语
	lang=langList[lang if(lang in langList)else 0]
	while True:
		if (userAns:=input(lang["ask"]))=="Y":print(lang["apply"]);return(True)
		elif userAns=="quit":print(lang["cancel"]);return(False)
		print(lang["reAsk"])