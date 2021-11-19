# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Taking inputs
P = int(input('Enter the value of load at in N(Newtons): '))
L = int(input('Enter the length of the beam AB in m(metres): '))
E = int(input('Enter the modulus of Elasticity of the beam in Pa(Pascals): '))
I = int(input('Enter I (the moment of inertia of the cross section of the beam about its neutral axis) in kg*m^2: '))
print('You have entered: P = ',P,'N, L = ',L,'m, E = ',E,'Pa, I = ',I, 'kg*m^2')

# Calculating Deflection and Slope at A:
y_a = -1 * P * L**3 / (3 * E * I)
theta_a =  P * L**2 / (2 * E * I)
print('The deflection of the beam at A is ', y_a, 'm')
print('The angle of the beam at A is ', theta_a, 'radians')

# Equations for the deflection and slope of the beam
def y(x):
    return P * (-x**3 + 3*x*L**2 - 2*L**3) / (6*E*I)
def theta(x):
    return (-(P*x**2)/2 + (P*L**2)/2) / (E*I)

print(theta(0))

# Plotting the graphs for Deflection and Slope
l=np.linspace(0,L,1000)
X=[]
deflections_list=[]
slopes_list=[]
for x in l:
  X.append(x)
  deflections_list.append(y(x))
  slopes_list.append(theta(x))

# Deflection plot
plt.subplot(1,1,1)
plt.plot(X,deflections_list,color='m')
plt.plot([0,L],[0,0],color='y')
plt.title("Deflection of beam")
plt.xlabel("x (in m)")
plt.ylabel("Deflection (in m)")
plt.show()

#  Slope Plot
plt.subplot(1,1,1)
plt.plot(X,slopes_list,color='b')
plt.plot([0,L],[0,0],color='y')
plt.title("Slope of beam")
plt.xlabel("x (in m)")
plt.ylabel("Slope (in radians)")
plt.show()