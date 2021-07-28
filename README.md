# Quadratic interpolation
The Python program with PyQt wich allows to find function minimal and see the countur plot.
On input is given starting point (Punkt startowy), direction d0 (Kierunek d0), acurracy (E), number of iterations (L) and function (Funkcja).
In left box is show the result for each iteration, stop criteria and minimum x.

The program interface is in polish language.

## Example usage
### Linear function sin and cos
![equation](https://latex.codecogs.com/svg.latex?f(x)=\sin{x_1}+\cos{x_2})

where minimum is 

![equation](https://latex.codecogs.com/svg.latex?(x_1,x_2)=\left(2\pi%20k_1-\frac{\pi}{2},2\pi%20k_{2}+\cos^{-1}\left(\cos%20\left(2%20\pi%20k_{1}\right)-2\right)\right)) .
 
![alt text](https://user-images.githubusercontent.com/50682521/127311673-9b255848-9930-4de3-8ce0-d18b347b55a8.png)


### Function with many minimal points

![equation](https://latex.codecogs.com/svg.latex?f(x)=x_1^4+x_2^4-x_1^2-x_2^2) 

 where minimum is -0.5 in points 
 
 ![equation](https://latex.codecogs.com/svg.latex?(\mathrm{x}_1,%20\mathrm{x}_2)=\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right))
 
 ![equation](https://latex.codecogs.com/svg.latex?(\mathrm{x}_1,\mathrm{x}_2)=\left(-\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)).
 
 ![alt text](https://user-images.githubusercontent.com/50682521/127311671-d413d262-3072-4826-ad3b-16718ccbe480.png)
 
 ### Function with lim in minus infinitive

![equation](https://latex.codecogs.com/svg.latex?f(x)=x_1^2+x_2^2-(x_1x_2)^2) 

 where minimum is in 
 
 ![equation](https://latex.codecogs.com/svg.latex?-\infty).
 
 ![alt text](https://user-images.githubusercontent.com/50682521/127311667-f4a4510d-d2d8-4ef8-9ba8-bef4611bf469.png)
