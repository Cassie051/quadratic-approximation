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
        self.x012 = []

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

    def minimum(self,x0,x1,x2):
        numberOfIterations = 0
        currXMin = self.x_a        
        x = [x0, x1, x2]        
        y = [self.F_goal(x0), self.F_goal(x1), self.F_goal(x2)]
        while True:
            numberOfIterations += 1
            self.iterations = numberOfIterations
            self.x012.append(x)
            Licznik = y[0] * (x[1]**2-x[2]**2) + y[1] * (x[2]**2-x[0]**2) + y[2] * (x[0]**2-x[1]**2)
            Mianownik = 2 * (y[0] * (x[1]-x[2]) + y[1] * (x[2]-x[0]) + y[2] * (x[0]-x[1]))
            checkIfzero = np.where(Mianownik == 0)
            if(checkIfzero[0].size != 0):
                self.iterations -= 1
                return currXMin
            xMin = Licznik/Mianownik
            indexOfMaxValue = np.argmax(y)
            x[indexOfMaxValue] = xMin
            y[indexOfMaxValue] = self.F_goal(xMin)
            for i in range(0,len(x)):
                for j in range(1,len(x)):
                    if(x[j-1][0] > x[j][0]):
                        t = x[j-1]
                        x[j-1] = x[j]
                        x[j] = t
                        t= y[j-1]
                        y[j-1] = y[j]
                        y[j] = t
            
            self.vector_xm.append(xMin)
            self.value_xm.append(self.F_goal(xMin))
            self.critical.append(abs(self.F_goal(currXMin) - self.F_goal(xMin)))
            if(abs(self.F_goal(currXMin) - self.F_goal(xMin))< self.E2 or numberOfIterations>= self.L):
                break
            
            currXMin = xMin
        return xMin

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
                x = np.linspace( -5, 5, self.L)
                y = np.linspace( -5, 5, self.L)

                X, Y = np.meshgrid(x,y)

                step = 2
                x_1, x_2 = self.setupControls(step)

                result = self.minimum(self.x_a,x_1,x_2)

                if(result.all() == None):
                    return self.x012, self.vector_xm, self.value_xm, result, result, self.F_goal(self.x_a), self.critical, self.iterations 
                
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
                        return self.x012, self.vector_xm, self.value_xm, result, self.F_goal(result), self.F_goal(self.x_a), self.critical, self.iterations 
                    else:
                        self.canvas.axes.clear()
                        self.canvas.draw()
                        return self.x012, self.vector_xm, self.value_xm, result, self.F_goal(result), self.F_goal(self.x_a), self.critical, self.iterations
                except:
                    msg = QMessageBox()
                    msg.setInformativeText('Wystąpił nieoczekiwany błąd przy rysowaniu!')
                    msg.setWindowTitle("Błąd")
                    msg.exec_()
            except:
                msg = QMessageBox()
                msg.setInformativeText('Podano nieprawidłową funkcję!',x_1,x_2)
                msg.setWindowTitle("Błąd")
                msg.exec_()
        else:
             msg = QMessageBox()
             msg.setInformativeText('Nie podano kierunku!')
             msg.setWindowTitle("Błąd")
             msg.exec_()


if __name__ == "__main__":
    import sys
    