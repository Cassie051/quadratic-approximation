from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import parser

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
        if len(self.x_a) == 2:
            if self.d0[0]-self.x_a[0]==0:
                if dir == 1:
                    p.append(px+int(np.random.rand()*10+5))
                elif dir == 2:
                    p.append(px+int(np.random.rand()*10+15))
                elif dir == 3:
                    p.append(px-int(np.random.rand()*10+5))
                elif dir == 4:
                    p.append(px-int(np.random.rand()*10+15))
            elif self.d0[1]-self.x_a[1]==0:
                p.append(self.d0[1])
            else:
                p.append((self.d0[1]-self.x_a[1])*px / (self.d0[0]-self.x_a[0]) +
                     self.x_a[1] - (self.d0[1]-self.x_a[1])*self.x_a[0] / (self.d0[0]-self.x_a[0]))
        elif len(self.x_a) == 3:
            dx = self.d0[0]-self.x_a[0]  # xd-xa
            dy = self.d0[1]-self.x_a[1]  # yd-ya
            dz = self.d0[2]-self.x_a[2]  # zd-za
            p.append((px-self.x_a[0]) * dy/dx + self.x_a[1])
            p.append((px-self.x_a[0]) * dz/dx + self.x_a[2])
        return p

    def F_goal(self, p):
        code = parser.expr(self.formula).compile()
        len_p = len(p)
        if len_p == 2:
            x1 = p[0]
            x2 = p[1]
            out = eval(code)
        return out

    def minimum3D(self, a_prev,b_prev,d_prev):
        if d_prev[0]-a_prev[0] == 0 and d_prev[1]>a_prev[1]:
            dir = 1
        elif d_prev[0]-a_prev[0]==0 and d_prev[1]<a_prev[1]:
            dir = 3
        else:
            dir = 0
        a = a_prev
        b = b_prev
        d = d_prev
        l = 0
        tab = [a, b, d]
        tab.sort()
        a = tab[0]
        b = tab[1]
        d = tab[2]
        fa=self.F_goal(a)
        fb=self.F_goal(b)
        fd=self.F_goal(d)
        while (d[0]-a[0]>=self.E2) or l != self.L:       

            a_prev = a
            b_prev = b
            d_prev = d

            Lx1 = fa*(b[0]**2-d[0]**2)+fb*(d[0]**2-a[0]**2)+fd*(a[0]**2-b[0]**2)
            Mx1 = 2*(fa*(b[0]-d[0])+fb*(d[0]-a[0])+fd*(a[0]-b[0]))

            if Mx1<0 :
                p1 = Lx1/Mx1
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
            x_d = self.line(self.x_a[0]+int(np.random.rand()*10+20),0)
        # oś OX: A > b > d oraz II i III ćwiartka:
        elif (self.d0[1]-self.x_a[1]==0 and self.d0[0]<self.x_a[0]) or (self.d0[0]<self.x_a[0] and self.d0[1]>self.x_a[1]) or (self.d0[0]<self.x_a[0] and self.d0[1]<self.x_a[1]):
            x_b = self.line(self.x_a[0]-int(np.random.rand()*10+10),0)
            x_d = self.line(self.x_a[0]-int(np.random.rand()*10+20),0)
        # oś OY: A < b < d 
        elif self.d0[0]-self.x_a[0]==0 and self.d0[1]>self.x_a[1]:
            x_b = self.line(self.x_a[0],1)
            x_d = self.line(self.x_a[0],2)
        # oś OY: A > b > d
        elif self.d0[0]-self.x_a[0]==0 and self.d0[1]<self.x_a[1]:
            x_b = self.line(self.x_a[0],3)
            x_d = self.line(self.x_a[0],4)
        return x_b,x_d     

    def rysuj(self, start, direction, estimation, literation, set_function, ):
        self.canvas.axes = self.canvas.figure.add_subplot(111)

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
                x = np.linspace( -self.d0[0]-30, self.d0[0]+30, self.L)
                y = np.linspace( -self.d0[1]-30, self.d0[1]+30, self.L)

                X, Y = np.meshgrid(x,y)

                funkcja = self.formula
                funkcja = funkcja.replace("x1","X")
                funkcja = funkcja.replace("x2","Y")
                Z = eval(funkcja)

                x_b,x_d=self.setupControls()

                result = self.minimum3D(self.x_a,x_b,x_d)

                if(result == None):
                    return self.vector_xm, result

                self.canvas.axes.clear()

                self.canvas.axes.contourf(X, Y, Z, 40, cmap = "gist_earth", extend='both')

                self.canvas.axes.set_title('Warstwice')
                self.canvas.draw()
                try:
                    xm_x1= []
                    xm_x2= []
                    for i in range(len(self.vector_xm)):
                        xm_x1.append(self.vector_xm[i][0])
                        xm_x2.append(self.vector_xm[i][1])
                        if(i==0):
                            self.canvas.axes.scatter(self.x_a[0],self.x_a[1],c="pink")
                        self.canvas.axes.scatter(self.vector_xm[i][0],self.vector_xm[i][1],c="red")
                    self.canvas.axes.plot(xm_x1,xm_x2)
                    self.canvas.draw()
                    return self.vector_xm, result
                except:
                    msg = QMessageBox()
                    msg.setText("Błąd")
                    msg.setInformativeText('Wystąpił nieoczekiwany błąd przy rysowaniu!')
                    msg.setWindowTitle("Błąd")
                    msg.exec_()
            except:
                msg = QMessageBox()
                msg.setText("Błąd")
                msg.setInformativeText('Nie podano funkcji!')
                msg.setWindowTitle("Błąd")
                msg.exec_()
        else:
             msg = QMessageBox()
             msg.setText("Błąd")
             msg.setInformativeText('Nie podano kierunku!')
             msg.setWindowTitle("Błąd")
             msg.exec_()

    