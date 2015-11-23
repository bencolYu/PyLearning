#!/usr/bin/env python

import threading

from time import sleep, ctime

loops=[4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args

    def __call__(self):
       # apply(self.func,self.args)
       #self.func(self.args[0],self.args[1])
       self.func(*self.args)



def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())

def main():
    print('starting at:',ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
       # t=threading.Thread(target=loop,args=(i,loops[i]))
        t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at:',ctime())

if __name__=='__main__':
    main()







"""
import threading
from time import sleep, ctime

def loop0():
    print('start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 done at:',ctime())

def loop1():
    print('start loop  1 at:',ctime())
    sleep(2)
    print('loop1 done at:',ctime())

def main():
    print('starting at:',ctime())
    threading._start_new_thread(loop0(),())
    threading._start_new_thread(loop1(),())
    sleep(6)
    print('all done at:',ctime())

if __name__=='__main__':
    main()
"""
