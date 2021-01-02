import itertools
import sys

n=int(input())

def three(n):
    if n%3==0:
        print(0)
        return

    sn=str(n)
    keta=len(sn)

    num=0
    l0=[]
    l1=[]
    l2=[]
    for i in range(keta):
        nb=int(sn[i])
        num+=nb
        if nb%3==0:
            l0.append(nb)
        elif nb%3==1:
            l1.append(nb)
        else:
            l2.append(nb)
    
    if num%3==1:
        if len(l1)>=1 and len(sn)>1:
            print(1)
            return
        elif len(l2)>=2 and len(sn)>2:
            print(2)
            return
        else:
            print(-1)
            return
    elif num%3==2:
        if len(l2)>=1 and len(sn)>1:
            print(1)
            return
        elif len(l1)>=2 and len(sn)>2:
            print(2)
            return
        else:
            print(-1)
            return

three(n)