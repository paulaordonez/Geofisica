import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2000,2000,20000)
pc=3000.0
pe=2500.0
g=6.67*(10**-11)
r=800.0
z1=200.0
z2=300.0
z3=500.0


def c1(z1):
	c1= 2*np.pi*g*(r**2)*(pc-pe)*(z1/((x**2)+(z1**2)))
	return c1
maximo1= np.max(c1(z1))
half1= maximo1/2.0
def find_x1(z1):
	b1= (abs(((2*np.pi*g*(r**2)*(pc-pe)*z1)/(0.000335270684165))-(z1**2)))**0.5
	return b1

def c2(z2):
	c2= 2*np.pi*g*(r**2)*(pc-pe)*(z2/((x**2)+(z2**2)))
	return c2
def find_x2(z2):
	b2= (abs(((2*np.pi*g*(r**2)*(pc-pe)*z2)/(0.00022351382049))-(z2**2)))**0.5
	return b2
maximo2= np.max(c2(z2))
half2= maximo2/2.0


def c3(z3):
	c3= 2*np.pi*g*(r**2)*(pc-pe)*(z3/((x**2)+(z3**2)))
	return c3
maximo3= np.max(c3(z3))
half3= maximo3/2.0
def find_x3(z3):
	b3= (abs(((2*np.pi*g*(r**2)*(pc-pe)*z3)/(0.000134108301832))-(z3**2)))**0.5
	return b3

print "half1", half1
print "half2", half2
print "half3", half3
print "width1", find_x1(z1)
print "width2", find_x2(z2)
print "width3", find_x3(z3)
plt.plot(x,c1(z1), label="200", color="blue")
plt.plot(x,c2(z2), label="300", color="green")
plt.plot(x,c3(z3), label="500", color="red")
plt.xlabel("Distancia en metros")
plt.ylabel("Anomalia en Gal")
plt.title("Cilindro a distinta profundidad")
plt.legend(loc="best")
plt.savefig("cilindros.jpg")
