#coding=utf-8
from pywinauto import application,Desktop
import pywinauto
from time import sleep
import sys

#var = sys.argv[1]
var = 'SKU-003-001'
app = application.Application().start(r'C:\QAD\QAD-HIST\container\QAD.Client.exe',None)
app = application.Application().connect(path=r'C:\QAD\QAD-HIST\container\QAD.Client.exe')
dlg = app.window(title='登录')
dlg.wait('visible',timeout=5)
dlg['登录Edit'].type_keys('a044')
dlg.type_keys('{TAB 1}')
dlg.type_keys('20140960')
dlg['确定'].click()
newdlg = Desktop(backend='win32')['qadui: CCJX Domain CCJX [RMB] > CCJX 捷和电机(江西)有限公司 (1) - QAD Enterprise Applications']
newdlg.wait('visible',timeout=5)
newdlg['Edit'].type_keys('13.7')
sleep(0.5)
newdlg['Edit'].type_keys('{ENTER 1}')
newdlg2 = Desktop(backend='win32')['qadui: CCJX Domain CCJX [RMB] > CCJX 捷和电机(江西)有限公司 (2) - QAD Enterprise Applications']
sleep(2)
ui = newdlg2.window(title = '物料用途表查询',class_name='WindowsForms10.Window.8.app.0.83a9e6_r15_ad1')
newdlg2.wait('visible',timeout=10)
newdlg2.maximize()
ui.type_keys(var)
ui.type_keys('{ENTER 2}')
sleep(2)
newdlg2.click(button='left',pressed='',coords=(500,500),double=False,absolute=False)
newdlg2.type_keys('^a')
newdlg2.type_keys('^c')
qad3 = Desktop(backend='win32')['qadui: CCJX Domain CCJX [RMB] > CCJX 捷和电机(江西)有限公司 (3) - QAD Enterprise Applications']
#print(qad3.print_control_identifiers())

"""
newdlg['Edit'].type_keys('{ENTER 1}')
sleep(0.5)
newdlg.type_keys(var)
sleep(0.2)
newdlg.type_keys('{ENTER 1}')
sleep(0.2)
newdlg.type_keys('{ENTER 1}',with_spaces=True, set_foreground=True)
sleep(0.2)
newdlg.type_keys('^A')
sleep(2)
newdlg.type_keys('^C')
"""
'''
app = application.Application().start(r'C:\QAD\QAD-HIST\QAD-Hist.exe',None)
sleep(0.5)
app = application.Application().connect(title=r'欢迎使用QAD-Hist系统')
dlg = app.window(title_re='.*?QAD-Hist.*?')
sleep(0.5)
dlg['登录Edit'].set_focus()
dlg['用户名：Edit'].type_keys('a044')
sleep(0.5)
dlg['密码：Edit'].type_keys('20140960')
sleep(0.5)
dlg['Button2'].click()
sleep(15)
dlg2 = Desktop(backend='uia')
print(dlg2.print_control_identifiers())
'''

