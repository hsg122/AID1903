from socket import *
from select import *
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
rlist=[s]
wlist=[ ]
xlist=[ ]

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c,addr=r.accept()
            print('connect from ',addr)
            rlist.append(c)
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)

    for w in wlist:
        w.send('thank'.encode())
        wlist.remove(w)