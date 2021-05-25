from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import parser
from sympy import *


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.vector_xm = []
        self.x_a = []
        self.d0 = []

        self.E2 = 0
        self.L = 0

        self.formula = ""

        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas.axes.clear()

    def line(self, px,dir):
        p=[]
        p.append(px)

        if self.d0[0]-self.x_a[0]==0:
            if dir == 1 or dir == 2 or dir ==3 or dir==4 or dir==5:
                p.append(px+int(np.random.rand()*10+5*dir))
            elif dir == 6 or dir==7 or dir==8 or dir==9 or dir==10:
                p.append(px-int(np.random.rand()*10+5*(dir-5)))
        elif self.d0[1]-self.x_a[1]==0:
            p.append(self.d0[1])
        else:
            p.append((self.d0[1]-self.x_a[1])*px / (self.d0[0]-self.x_a[0]) +
                self.x_a[1] - (self.d0[1]-self.x_a[1])*self.x_a[0] / (self.d0[0]-self.x_a[0]))
        return p

    def F_goal(self, p):
        code = parser.expr(self.formula).compile()
        x1 = p[0]
        x2 = p[0]
        x3 = p[0]
        x4 = p[0]
        x5 = p[0]
        out = eval(code)
        return out
    
    def minimum3D(self, a_prev,b_prev,d_prev,c_prev,e_prev,g_prev,xlen):
        if d_prev[0]-a_prev[0] == 0 and d_prev[1]>a_prev[1]:
            dir = 1
        elif d_prev[0]-a_prev[0]==0 and d_prev[1]<a_prev[1]:
            dir = 3
        else:
            dir = 0
        a = a_prev
        b = b_prev
        c = c_prev
        e = e_prev
        g = g_prev
        d = d_prev
        l = 0

        tab = [a, b, c, e, g, d]
        tab.sort()
        a = tab[0]
        b = tab[1]
        c = tab[2]
        e = tab[3]
        g = tab[4]
        d = tab[5]
        fa=self.F_goal(a) 
        fb=self.F_goal(b) # do x1, x2
        fc=self.F_goal(c) # dodawany gdy mamy x3
        fe=self.F_goal(e) # dodawany gdy mamy x4
        fg=self.F_goal(g) # dodawany gdy mamy x5
        fd=self.F_goal(d) # do x1, x2
        while (d[0]-a[0]>=self.E2) or l != self.L:      
            a_prev = a
            b_prev = b
            c_prev = c
            e_prev = e
            g_prev = g
            d_prev = d
            # Lx1 = fa*(b[0]**2-d[0]**2)+fb*(d[0]**2-a[0]**2)+fd*(a[0]**2-b[0]**2)
            # Mx1 = 2*(fa*(b[0]-d[0])+fb*(d[0]-a[0])+fd*(a[0]-b[0]))
            if xlen==2:
            # Lx1 = fa*(b[0]**2-d[0]**2)+fb*(d[0]**2-a[0]**2)+fd*(a[0]**2-b[0]**2)
            # Mx1 = 2*(fa*(b[0]-d[0])+fb*(d[0]-a[0])+fd*(a[0]-b[0]))
            # pom = Lx1/Mx1
                x = symbols('x')
                part_fa = fa*(x-b[0])*(x-d[0])/((a[0]-b[0])*(a[0]-d[0]))
                part_fb = fb*(x-a[0])*(x-d[0])/((b[0]-a[0])*(b[0]-d[0]))
                part_fd = fd*(x-a[0])*(x-b[0])/((d[0]-a[0])*(d[0]-b[0]))
                fun = part_fa+part_fb+part_fd
                derivative_prim = fun.diff(x)
                eq = Eq(derivative_prim)
                sol=solve(eq,x)
                derivative_bis =  derivative_prim.diff(x)
                der = derivative_bis
            if xlen==3:
                x = symbols('x')
                part_fa = fa*(x-b[0])*(x-d[0])*(x-c[0])/((a[0]-b[0])*(a[0]-d[0])*(a[0]-c[0]))
                part_fb = fb*(x-a[0])*(x-d[0])*(x-c[0])/((b[0]-a[0])*(b[0]-d[0])*(b[0]-c[0]))
                part_fc = fc*(x-a[0])*(x-b[0])*(x-d[0])/((c[0]-a[0])*(c[0]-b[0])*(c[0]-d[0])) 
                part_fd = fd*(x-a[0])*(x-b[0])*(x-c[0])/((d[0]-a[0])*(d[0]-b[0])*(d[0]-c[0]))
                fun = part_fa+part_fb+part_fc+part_fd
                derivative_prim = fun.diff(x)
                eq = Eq(derivative_prim)
                sol=solve(eq,x)
                derivative_bis =  derivative_prim.diff(x)
                derivative_tri =  derivative_bis.diff(x)
                der = derivative_tri
            if xlen==4:
                x = symbols('x')
                part_fa = fa*(x-b[0])*(x-d[0])*(x-c[0])*(x-e[0])/((a[0]-b[0])*(a[0]-d[0])*(a[0]-c[0])*(a[0]-e[0]))
                part_fb = fb*(x-a[0])*(x-d[0])*(x-c[0])*(x-e[0])/((b[0]-a[0])*(b[0]-d[0])*(b[0]-c[0])*(b[0]-e[0]))
                part_fc = fc*(x-a[0])*(x-b[0])*(x-d[0])*(x-e[0])/((c[0]-a[0])*(c[0]-b[0])*(c[0]-d[0])*(c[0]-e[0])) 
                part_fe = fe*(x-a[0])*(x-b[0])*(x-d[0])*(x-c[0])/((e[0]-a[0])*(e[0]-b[0])*(e[0]-d[0])*(e[0]-c[0])) 
                part_fd = fd*(x-a[0])*(x-b[0])*(x-c[0])*(x-e[0])/((d[0]-a[0])*(d[0]-b[0])*(d[0]-c[0])*(d[0]-e[0]))
                fun = part_fa+part_fb+part_fc+part_fe+part_fd
                derivative_prim = fun.diff(x)
                eq = Eq(derivative_prim)
                sol=solve(eq,x)
                derivative_bis =  derivative_prim.diff(x)
                derivative_tri =  derivative_bis.diff(x)
                derivative_quatro =  derivative_tri.diff(x)
                der = derivative_quatro
            if xlen==5:
                x = symbols('x')
                part_fa = fa*(x-b[0])*(x-d[0])*(x-c[0])*(x-e[0])*(x-g[0])/((a[0]-b[0])*(a[0]-d[0])*(a[0]-c[0])*(a[0]-e[0])*(a[0]-g[0]))
                part_fb = fb*(x-a[0])*(x-d[0])*(x-c[0])*(x-e[0])*(x-g[0])/((b[0]-a[0])*(b[0]-d[0])*(b[0]-c[0])*(b[0]-e[0])*(b[0]-g[0]))
                part_fc = fc*(x-a[0])*(x-b[0])*(x-d[0])*(x-e[0])*(x-g[0])/((c[0]-a[0])*(c[0]-b[0])*(c[0]-d[0])*(c[0]-e[0])*(c[0]-g[0])) 
                part_fe = fe*(x-a[0])*(x-b[0])*(x-d[0])*(x-c[0])*(x-g[0])/((e[0]-a[0])*(e[0]-b[0])*(e[0]-d[0])*(e[0]-c[0])*(e[0]-g[0])) 
                part_fg = fg*(x-a[0])*(x-b[0])*(x-d[0])*(x-c[0])*(x-e[0])/((g[0]-a[0])*(g[0]-b[0])*(g[0]-d[0])*(g[0]-c[0])*(g[0]-e[0])) 
                part_fd = fd*(x-a[0])*(x-b[0])*(x-c[0])*(x-e[0])*(x-g[0])/((d[0]-a[0])*(d[0]-b[0])*(d[0]-c[0])*(d[0]-e[0])*(d[0]-g[0]))
                fun = part_fa+part_fb+part_fc+part_fe+part_fg+part_fd
                derivative_prim = fun.diff(x)
                eq = Eq(derivative_prim)
                sol=solve(eq,x)
                derivative_bis =  derivative_prim.diff(x)
                derivative_tri =  derivative_bis.diff(x)
                derivative_quatro =  derivative_tri.diff(x)
                derivative_funto =  derivative_quatro.diff(x)
                der = derivative_funto
            if der>0 :
                p1 = float(sol[0])
                p = self.line(p1,dir)
                self.vector_xm.append(p)
                F_x = self.F_goal(p)
                if (np.sqrt((p[0]-a[0])**2+(p[1]-a[1])**2)<self.E2) or (np.sqrt((p[0]-b[0])**2+(p[1]-b[1])**2)<self.E2) or (np.sqrt((p[0]-d[0])**2+(p[1]-d[1])**2)<self.E2):
                    if F_x < fb:
                        print('kontrola 1')
                        return p
                    else:
                        print('kontrola 2')
                        return b
                elif p[0] > a[0] and p[0] < d[0] :
                    if p[0] < b[0]:
                        if F_x < fb:
                            a = a_prev
                            b = p
                            d = b_prev
                            fd = fb
                            fb = F_x
                            l += 1
                            print('kontrola 3')
                        elif F_x>=fb:
                            a = p
                            b = b_prev
                            d = d_prev
                            fa = F_x
                            l += 1
                            print('kontrola 4')
                    else:
                        if F_x < fb:
                            a = b_prev
                            b = p
                            d = d_prev
                            fa = fb
                            fb = F_x
                            l += 1
                            print('kontrola 5')
                        elif F_x >= fb:
                            a = a_prev
                            b = b_prev
                            d = p
                            fd = F_x
                            l += 1
                            print('kontrola 6')
                    if d[0]-a[0]<self.E2:
                        if F_x<fb:
                            print('kontrola 7')
                            return p
                        else:
                            print('kontrola 8')
                            return b
                else:
                    msg = QMessageBox()
                    msg.setText("Błąd")
                    msg.setInformativeText("Optymalizacja nie powiodla sie - znalezione minimum poza badanych przedzialem")
                    msg.setWindowTitle("Błąd")
                    msg.exec_()
                    return None
            else:
                msg = QMessageBox()
                msg.setText("Błąd")
                msg.setInformativeText("Optymalizacja nie powiodla sie - znaleziono maksimum lub punkt siodłowy funkcji aproksymującej")
                msg.setWindowTitle("Błąd")
                msg.exec_()
                return None


    def setupControls(self):
        # oś OX: A < b < d oraz I i IV ćwiartka:
        if (self.d0[1]-self.x_a[1]==0 and self.d0[0]>self.x_a[0]) or (self.d0[0]>self.x_a[0] and self.d0[1]>self.x_a[1]) or (self.d0[0]>self.x_a[0] and self.d0[1]<self.x_a[1]):
            x_b = self.line(self.x_a[0]+int(np.random.rand()*10+10),0)
            x_c = self.line(self.x_a[0]+int(np.random.rand()*10+15),0)
            x_e = self.line(self.x_a[0]+int(np.random.rand()*10+20),0)
            x_g = self.line(self.x_a[0]+int(np.random.rand()*10+25),0)
            x_d = self.line(self.x_a[0]+int(np.random.rand()*10+30),0)
        # oś OX: A > b > d oraz II i III ćwiartka:
        elif (self.d0[1]-self.x_a[1]==0 and self.d0[0]<self.x_a[0]) or (self.d0[0]<self.x_a[0] and self.d0[1]>self.x_a[1]) or (self.d0[0]<self.x_a[0] and self.d0[1]<self.x_a[1]):
            x_b = self.line(self.x_a[0]-int(np.random.rand()*10+10),0)
            x_c = self.line(self.x_a[0]-int(np.random.rand()*10+15),0)
            x_e = self.line(self.x_a[0]-int(np.random.rand()*10+20),0)
            x_g = self.line(self.x_a[0]-int(np.random.rand()*10+25),0)
            x_d = self.line(self.x_a[0]-int(np.random.rand()*10+30),0)
        # oś OY: A < b < d 
        elif self.d0[0]-self.x_a[0]==0 and self.d0[1]>self.x_a[1]:
            x_b = self.line(self.x_a[0],1)
            x_c = self.line(self.x_a[0],2)
            x_e = self.line(self.x_a[0],3)
            x_g = self.line(self.x_a[0],4)
            x_d = self.line(self.x_a[0],5)
        # oś OY: A > b > d
        elif self.d0[0]-self.x_a[0]==0 and self.d0[1]<self.x_a[1]:
            x_b = self.line(self.x_a[0],6)
            x_c = self.line(self.x_a[0],7)
            x_e = self.line(self.x_a[0],8)
            x_g = self.line(self.x_a[0],9)
            x_d = self.line(self.x_a[0],10)
        return x_b,x_d,x_c,x_e,x_g     

    def rysuj(self, start, direction, estimation, literation, set_function ):
        self.canvas.axes.clear()

        self.vector_xm = []
        self.x_a = [float(x) for x in start.split(',')]
        self.d0 = [float(x) for x in direction.split(',')]

        estimation = estimation.replace("^","**")

        self.E2 = eval(estimation)
        self.L = int(literation)

        set_function = set_function.replace("^","**")
        self.formula = set_function

        if len(self.d0) == 2:
            try:
                global i
                x = np.linspace( -self.d0[0]-40, self.d0[0]+40, self.L)
                y = np.linspace( -self.d0[1]-40, self.d0[1]+40, self.L)

                X, Y = np.meshgrid(x,y)

                funkcja = self.formula
                funkcja = funkcja.replace("x1","X")
                funkcja = funkcja.replace("x2","Y")
                Z = eval(funkcja)

                x_b,x_d,x_c,x_e,x_g = self.setupControls()
                value_xm = []

                result = self.minimum3D(self.x_a,x_b,x_d,x_c,x_e,x_g,2)

                if(result == None):
                    return self.vector_xm, value_xm, result, result, self.F_goal(self.x_a)

                self.canvas.axes.clear()

                self.canvas.axes.contourf(X, Y, Z, 40, cmap = "gist_earth", extend='both')

                self.canvas.axes.set_title('Warstwice')
                self.canvas.draw()
                try:
                    xm_x1= []
                    xm_x2= []
                    self.canvas.axes.scatter(self.x_a[0],self.x_a[1],c="pink")
                    for i in self.vector_xm:
                        value_xm.append(self.F_goal(i))
                    for i in range(len(self.vector_xm)):
                        xm_x1.append(self.vector_xm[i][0])
                        xm_x2.append(self.vector_xm[i][1])
                        self.canvas.axes.scatter(self.vector_xm[i][0],self.vector_xm[i][1],c="red")
                    self.canvas.axes.plot(xm_x1,xm_x2)
                    self.canvas.draw()
                    return self.vector_xm, value_xm, result, self.F_goal(result), self.F_goal(self.x_a)
                except:
                    msg = QMessageBox()
                    msg.setInformativeText('Wystąpił nieoczekiwany błąd przy rysowaniu!')
                    msg.setWindowTitle("Błąd")
                    msg.exec_()
            except:
                msg = QMessageBox()
                msg.setInformativeText('Podano nieprawidłową funkcję!')
                msg.setWindowTitle("Błąd")
                msg.exec_()
        else:
             msg = QMessageBox()
             msg.setInformativeText('Nie podano kierunku!')
             msg.setWindowTitle("Błąd")
             msg.exec_()

    