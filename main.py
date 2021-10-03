import sys
import time

p = "w"
n = " "

def _pl(wr,e,w,c):
    i = 0
    s = ""
    while True:
        if i >= e-c:
            break
        s+=n
        wr(s)
        i+=1
    while True:
        if i >= c+e+1:
            break
        s+=p
        wr(s)
        i+=1
    while True:
        if i >= w:
            break
        s+=n
        wr(s)
        i+=1

def wp(e,usp,dsp):
    wr = lambda _: sys.stdout.write("\r"+_) and (sys.stdout.flush() or time.sleep(0.001))
    while usp > 0:
        i = 0
        l = ""
        while True:
            if i == 2 * e + 1:
                break
            l += n
            i += 1
            wr(l)
        wr(l+'\n')
        usp-=1
    i = 0
    while i < (2 * e + 1)*0.15 :
        _pl(wr,e,2 * e + 1,i)
        wr('\n')
        i+=1
    while dsp > 0:
        i = 0
        l = ""
        while True:
            if i == 2 * e + 1:
                break
            l += n
            i += 1
            wr(l)
        wr(l+'\n')
        dsp-=1

wp(15,1,1)