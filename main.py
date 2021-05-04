import sys 
sys.path.append(r'c:\users\alusia\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages')
import numpy as np
import matplotlib.pyplot as plt


# informacje wejściowe
a_k = [] # tablica lewych krańców przedziałów (pierwszy punkt próbny)
b_k = [] # tablica prawych końców przedziałów (trzeci punkt próbny)
c_k = [] # tablica drugich punktów próbnych
x_k = [] # punkty zerowania się pierwszej pochodnej funkcji aproksymującej
a0 = 0 # lewy kraniec początkowego przedziału poszukiwań
b0 = 2 # prawy kraniec początkowego przedziału poszukiwań
x = np.linspace(a0*np.pi,b0*np.pi,1000000) # wartości na przedziale [a,b]
E = 10**(-4) #epsilon, wymagana dokładność (graniczna długość odcinka, minimalna odległość x od punktów próbnych)

def f_x2(x,a,b,c):
    f_x = F_a * (x - a) * (x - b) / ((a - c) * (a - b)) + F_c * (x - a) * (x - b) / ((c - a) * (c - b)) + F_b * (x - a) * (x - c) / ((b - a) * (b - c))
    return f_x

def x_kk(a,b,c,Fa,Fb,Fc):
    L = (b**2 - c**2) * Fa + (c**2 - a**2) * Fb + (a**2 - b**2) * Fc
    M = (c-b) * Fa + (a-c) * Fb + (b-a) * Fc
    if(M > 0):
        x = None
    else:
        x = 0.5 * L / M
    return x

# krok wstępny
a_k.append(a0) #podstawiamy a_1=a_0
b_k.append(b0) #podstawiamy b_1=b_0
c_pom = (a0 + b0)/2
c_k.append(c_pom)

f_x1 = np.exp(x)*np.sin(x) # nasza zadana funkcja

Fa = np.exp(a_k[0]) * np.sin(a_k[0])
Fb = np.exp(b_k[0]) * np.sin(b_k[0])
Fc = np.exp(c_k[0]) * np.sin(c_k[0])

x_pom = x_kk(a_k[0],b_k[0],c_k[0],Fa,Fb,Fc)

plt.figure()
plt.plot(f_x1)
plt.show()