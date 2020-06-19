"""
select 函数讲解
我来试一下第一次修改
"""
from select import *
from socket import *
print("listen iO ")
f=socket()
f.bind(('0.0.0.0',8888))
f.listen(3)
fd=open("log.txt",'a+')
rs,ws,xs=select([f],[fd],[fd])
print("rs",rs)
print("ws",ws)
print("xs",xs)


"second way"