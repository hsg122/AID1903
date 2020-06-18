"""
poll多路复用
"""
from socket import *
from select import *
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
#创建关注的IO
p=poll()
#建立字典{fileno: io_obj} 文件描述为键,套接字对qj为dic值
dict={s.fileno():s}
p.register(s,POLLIN|POLLERR)
while True:
    event=p.poll()
    print(event)
    for fd ,event in event:
        if fd==s.fileno():
            c,addr=dict[fd].accept()
            print('Connect from%s,%d'%(addr[0],addr[1]))
            #将套接字C加入POLL关注的范围 同时把套接字C加入字典
            p.register(c,POLLIN|POLLHUP)
            dict[c.fileno()] = c
        # 和是有零说零 所以EVENT和POLLHUP都为真时为真
        # elif event & POLLHUP:
        #     print('connect close')
        #     p.unregister(fd)
        #     dict[fd].close()
        #     del dict[fd]
        elif event&POLLIN:
            data=dict[fd].recv(1024)
            if not data:
                print('connect close')
                p.unregister(fd)
                dict[fd].close()
                del dict[fd]
                continue#跳过下面的两句break跳出循环 RETRUN跳出函数

            print(data.decode())
            dict[fd].send(b'ok')
