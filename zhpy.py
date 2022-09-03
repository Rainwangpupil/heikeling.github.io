import requests as r
import easygui as g
def 打印(p):
    print(p)
def 询问(x):
    input(x)
def 请求get(req):
    r.get(req)
def 请求post(post):
    r.post(post)
def 弹出(tc):
    g.msgbox(tc)
def 询问弹出(xw):
    g.enterbox(xw)
