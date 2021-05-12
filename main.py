import sys
sys.path.append(r'c:\users\alusia\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages')
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import *
from scipy import special
import parser
from math import sin

# INFORMACJE WEJŚCIOWE
x = np.linspace(0, 1, 1000)
f_x = np.sin(x)  # funkcja podana na wejściu, może mieć do 5 zmiennych
''' ogólnie może być f(x1) lub f(x1,x2) ....
    w tym wypadku potrzebujemy podać punkt startowy i tej samej ilości zmiennych
    np. dla f(x1) podamy a=(1), dla f(x1,x2) podamy a=(1,1) itd. ... '''
x_a = [
]  # punkt startowy (może być jednej zmiennej lub więcej), np. x_a = {1} lub x_a = {1,1} ...
x_a.append(0)  # tutaj przykład dla f(x)
x_a.append(0)
d0 = []  # kierunek optymalizacji (czyli punkt)
d0.append(1)
d0.append(1)

E2 = 10**(-4)  # nasze ograniczenie
L = 1000  # liczba iteracji

# SPRAWDZANIE CZY PUNKT NALEŻY DO PROSTEJ
''' a - punkt pocz.
    d - kierunek d0
    p - punkt do zrobienia'''


def line(a, d, px):
    p=[]
    p.append(px)
    if len(a) == 2:
        p.append((d[1]-a[1])*px / (d[0]-a[0]) +
                 a[1] - (d[1]-a[1])*a[0] / (d[0]-a[0]))
    elif len(a) == 3:
        dx = d[0]-a[0]  # xd-xa
        dy = d[1]-a[1]  # yd-ya
        dz = d[2]-a[2]  # zd-za
        p.append((px-a[0])*dy/dx+a[1])
        p.append((px-a[0])*dz/dx+a[2])
    return p
    
#INTERPOLACJA LAGRANGE'A (dla 2D, 3D, 4D, 5D)
def Lagrange(n, checkpoints):
    return 0

def F_goal(p,f):
    code = parser.expr(f).compile()
    len_p = len(p)
    if len_p == 2:
        x1 = p[0]
        x2 = p[1]
        out = eval(code)
    return out
        
def minimum3D(a_prev,b_prev,d_prev,fa,fb,fd,func):
    a = a_prev
    b = b_prev
    d = d_prev
    while d[0]-a[0]>=E2 and d[1]-a[1]>=E2:
        a_prev = a
        b_prev = b
        d_prev = d
        #det_BT = b[0]*d[1]+a[0]*b[1]+a[1]*d[0]-a[1]*b[0]-d[0]*b[1]-d[1]*a[0]
        # licznik x1m
        # Lx1 = -fa*(b[0]*d[1]-d[0]*b[1]+d[0]-b[0])-fb*(d[0]*a[1]-a[0]*d[1]+a[0]-d[0])-fd*(a[0]*b[1]-b[0]*a[1]+b[0]-a[0])
        # # mianownik x1m
        # Mx1 = fa*(b[1]-d[1])+fb*(d[1]-a[1])+fd*(a[1]-b[1])
        # # licznik x2m
        # Lx2 = -fa*(b[0]*d[1]-d[0]*b[1]+b[1]-d[1])-fb*(d[0]*a[1]-a[0]*d[1]+d[1]-a[1])-fd*(a[0]*b[1]-b[0]*a[1]+a[1]-b[1])
        # # mianownik x2m
        # Mx2 = fa*(d[0]-b[0])+fb*(a[0]-d[0])+fd*(b[0]-a[0])

        # x1m = Lx1/Mx1
        # x2m = Lx2/Mx2

        Lx1 = fa*(b[0]**2-d[0]**2)+fb*(d[0]**2-a[0]**2)+fd*(a[0]**2-b[0]**2)
        Mx1 = 2*(fa*(b[0]-d[0])+fb*(d[0]-a[0])+fd*(a[0]-b[0]))

        p1 = Lx1/Mx1
        p = line(a,d,p1)
        if Mx1<0 :
            # p=[]
            # p.append(xm1)
            # p.append(xm2)
            F_x = F_goal(p,func)
            if (np.sqrt((p[0]-a[0])**2+(p[1]-a[1])**2)<E2) or (np.sqrt((p[0]-b[0])**2+(p[1]-b[1])**2)<E2) or (np.sqrt((p[0]-d[0])**2+(p[1]-d[1])**2)<E2):
                if F_x < fb:
                    print('kontrola 1')
                    return p
                else:
                    print('kontrola 2')
                    return b
            elif p[0] > a[0] and x[0] < d[0] and p[1] > a[1] and x[1] < d[1]:
                if p[0] < b[0] and p[1] < b[1]:
                    if F_x < fb:
                        a = a_prev
                        b = p
                        d = b_prev
                        fd = fb
                        fb = F_x
                        print('kontrola 3')
                    elif F_x>=fb:
                        a = p
                        b = b_prev
                        d = d_prev
                        fa = F_x
                        print('kontrola 4')
                else:
                    if F_x < fb:
                        a = b_prev
                        b = p
                        d = d_prev
                        fa = fb
                        fb = F_x
                        print('kontrola 5')
                    elif F_x >= fb:
                        a = a_prev
                        b = b_prev
                        d = p
                        fd = F_x
                        print('kontrola 6')
                if d[0]-a[0]<E2 and d[1]-a[1]:
                    if F_x<fb:
                        print('kontrola 7')
                        return p
                    else:
                        print('kontrola 8')
                        return b
            else:
                return "Optymalizacja nie powiodla sie - znalezione minimum poza badanych przedzialem"
        else:
            return "Optymalizacja nie powiodla sie - znaleziono maksimum lub punkt siodłowy funkcji aproksymującej"


formula = "(x1-2)**2+(x2-2)**2"

x_b = line(x_a,d0,10)

x_d = line(x_a,d0,20)

Fa=F_goal(x_a,formula)
Fb=F_goal(x_b,formula)
Fd=F_goal(x_d,formula)

print(minimum3D(x_a,x_b,x_d,Fa,Fb,Fd,formula))

