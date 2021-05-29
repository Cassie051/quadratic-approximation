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
        self.value_xm = []
        self.critical = []
        self.x_a = []
        self.d0 = []

        self.E2 = 0
        self.L = 0
        self.iterations = 0 

        self.formula = ""

        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas.axes.clear()

    def F_goal(self,p):
        code = parser.expr(self.formula).compile()
        for i in range(1, len(p)+1):
            locals()['x%s' % i] = p[i-1]
        out = eval(code)
        return out

    def setupControls(self,step):
        x_1 = self.x_a +  step * self.d0
        if self.F_goal(self.x_a) > self.F_goal(x_1):
            x_2 = self.x_a + 2 * step * self.d0
        else:
            x_2 = x_1
            x_1 = self.x_a + 0.5 * step * self.d0
        x_2 = np.array(x_2)
        x_1 = np.array(x_1)
        return x_1,x_2

    def minimum(self,x_0,x_1,x_2):
        np.seterr(divide='ignore', invalid='ignore')
        l = 0
        x_min = x_2
        x_min_tab = []
        x_min_tab.append(x_0)
        while True:
            if np.linalg.norm(x_min_tab[-1]-x_min) <= self.E2 or l >= self.L:
                break
            print(np.linalg.norm(x_min_tab[-1]-x_min))
            f0 = self.F_goal(x_0)
            f1 = self.F_goal(x_1)
            f2 = self.F_goal(x_2)
            L_min = f0 * (x_1**2-x_2**2) + f1 * (x_2**2-x_0**2) + f2 * (x_0**2-x_1**2)
            M_min = 2 * (f0 * (x_1-x_2) + f1 * (x_2-x_0) + f2 * (x_0-x_1))
            x_min = L_min/M_min
            tab_f = [f0, f1, f2]
            max_f = np.amax(tab_f)
            max_x = tab_f.index(max_f)
            tab_x = np.array([x_0,x_1,x_2])
            tab_x[max_x] = x_min
            tab_x.sort(axis=0)
            x_0 = tab_x[0]
            x_1 = tab_x[1]
            x_2 = tab_x[2]
            self.vector_xm.append(x_min)
            print(x_min)
            print(self.vector_xm)
            self.value_xm.append(self.F_goal(x_min))
            self.critical.append(np.linalg.norm(x_min_tab[-1]-x_min))
            l += 1
            x_min_tab.append(x_min)
            self.iterations = l

        return x_min

    def rysuj(self, start, direction, estimation, literation, set_function ):
        self.canvas.axes.clear()

        self.vector_xm = []
        self.x_a = [float(x) for x in start.split(',')]
        self.d0 = [float(x) for x in direction.split(',')]
        self.x_a = np.array(self.x_a)
        self.d0 = np.array(self.d0)

        estimation = estimation.replace("^","**")

        self.E2 = eval(estimation)
        self.L = int(literation)

        set_function = set_function.replace("^","**")
        set_function = set_function.replace("cos","np.cos")
        set_function = set_function.replace("sin","np.sin")
        self.formula = set_function

        if len(self.d0) != 0:
            try:
                global i
                tab = [self.d0[0], self.d0[1], self.x_a[0], self.x_a[1]]
                max_val = max(tab)
                x = np.linspace( -self.x_a[0]-5*max_val, self.x_a[0]+5*max_val, self.L)
                y = np.linspace( -self.x_a[1]-5*max_val, self.x_a[1]+5*max_val, self.L)

                X, Y = np.meshgrid(x,y)

                step = 2
                x_1, x_2 = self.setupControls(step)

                result = self.minimum(self.x_a,x_1,x_2)

                if(result.all() == None):
                    return self.vector_xm, self.value_xm, result, result, self.F_goal(self.x_a), self.critical, self.iterations 
                
                try:
                    if(len(self.d0) == 2):
                        funkcja = self.formula
                        funkcja = funkcja.replace("x1","X")
                        funkcja = funkcja.replace("x2","Y")
                        Z = eval(funkcja)

                        self.canvas.axes.clear()
                        self.canvas.axes.contourf(X, Y, Z, 40, cmap = "gist_earth", extend='both')
                        self.canvas.axes.set_title('Warstwice')
                        self.canvas.draw()
                        xm_x1= []
                        xm_x2= []
                        self.canvas.axes.scatter(self.x_a[0],self.x_a[1],c="pink")
                        for i in range(len(self.vector_xm)):
                            xm_x1.append(self.vector_xm[i][0])
                            xm_x2.append(self.vector_xm[i][1])
                            self.canvas.axes.scatter(self.vector_xm[i][0],self.vector_xm[i][1],c="red")
                        xm_x1.append(self.x_a[0])
                        xm_x2.append(self.x_a[1])
                        self.canvas.axes.plot(xm_x1,xm_x2)
                        self.canvas.draw()
                        return self.vector_xm, self.value_xm, result, self.F_goal(result), self.F_goal(self.x_a), self.critical, self.iterations 
                    else:
                        self.canvas.figure.add_subplot(111)
                        self.canvas.axes.clear()
                        return self.vector_xm, self.value_xm, result, self.F_goal(result), self.F_goal(self.x_a), self.critical, self.iterations
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
