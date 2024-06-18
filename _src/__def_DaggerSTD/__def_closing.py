#def closing()

from types		import FunctionType as function
from tkinter	import Tk

def closing(saveFunc:function=None):
	###构造主窗口关闭函数
	#saveFunc	无参保存函数
	if not saveFunc:
		def _():
			print("mark_exit")
			from os import _exit
			_exit(0)
	else:
		def _():
			print("mark_saving_start")
			saveFunc()#保存函数使用环境变量参数,而不是传入的参数
			print("mark_saving_complete")
			print("mark_exit")
			from os import _exit
			_exit(0)
	return(_)
def	exitWhenClose(rootWindow:Tk,saveFunc:function=None):
	###重定向窗口的关闭函数,来实现正确关闭
	#rootWindow	需实现关闭即结束进程的主窗口
	#saveFunc	无参保存函数
	rootWindow.protocol("WM_DELETE_WINDOW",closing(saveFunc))