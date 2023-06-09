# Section 2
# Part 1

        #Create aircarft state space model

import numpy as np
import matplotlib.pyplot as plt

# Given values
V= 279.1    # Velocity ft/sec
rho = 0.002377  # Density slug/ft^3
S = 5500    # Wing area ft^2
c_bar = 27.3    # Mean chord length in ft
W = 564032     # Weight in lb
b = 195.7   # Wing span in ft
Ix = 14.3e6  # MOI about x axis in slug ft^2
Iy = 32.3e6  # MOI about y axis in slug ft^2
Iz = 45.3e6  # MOI about z axis in slug ft^2
Ixz = -2.23e6  # MOI about xz axis in slug ft^2

# Aerodynamic Derivatives
Cy_beta = -0.96
Cyp = 0.0
Cyr = 0.0
Cl_beta = -0.221
Clp = -0.45
Clr = 0.101
Cn_beta = 0.15
Cnp = -0.121
Cnr = -0.30

# Other aerodynamic derivatives
Cl_del_a = 0.0461
Cn_del_a = 0.0064
Cy_del_r = 0.175
Cl_del_r = 0.007
Cn_del_r = -0.109

#Conversion Factors
ft_to_m = 0.3048    # Conversion from ft to meters

#Calculate some important parameters
g = 32.174  # Accelration due to gravity in ft/sec^2
Q = 0.5 * rho * V**2    # Dynamic Pressure (lb/ft^2)
m = W / 32.174 #Mass (lb to slug)

# State vector x = [v  p  phi r]^T --> Column vector
# Control vector --> eta = [del_r    del_a]^T --> Column vector
# Sideslip angle is beta

# State space model matrices
A = np.array([[-Cy_beta*Q*S/(m*V), 0, 0, -m*g/(m*V)],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, (b * (Clp*Q*S*b + Cnp*Q*S*c_bar)) / (Iy*V), 0, (Clr*Q*S*b + Cnr*Q*S*c_bar) / (Iy*V)]])

B = np.array([[Cy_del_r*Q*S/m, Cl_del_a*Q*S / (Iy*V)],
              [0, 0],
              [0, 0],
              [Cn_del_r*Q*S*b / (Iy*V), Cn_del_a*Q*S*c_bar / (Iy*V)]])

C = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])

D = np.zeros((2, 2))

# Printing the state space model matrices
print("A matrix (System dynamics) :")
print(A)
print("\n")

print("B matrix (Influence of control vars on state vars:")
print(B)
print("\n")

print("C matrix: ")
print(C)
print("\n")

print("D matrix:")
print(D)

### Pole-zero map of the state-space plant

import control

sys = control.StateSpace(A, B, C, D)
Poles = sys.pole()
Zeroes = sys.zero()

## Printing poles and zeroes of system
print("Poles:")
for pole in Poles:
    print(pole)

print("\nZeroes:")
for zero in Zeroes:
    print(zero)

# No zeroes in the system

# To show a step response of roll rate given an input

# Define the time vector for simulation
t = np.linspace (0,10,1000)
# Define the input step function
u = np.ones_like(t)

# Simulate the system step response
t, y = control.step_response(sys, T=t, input=u)

# Reshape the y array to have a 1D shape
y = np.squeeze(y)
y = y[0]

#Plotting the step response

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Roll Rate')
plt.title('Step Response of Roll Rate')
plt.grid(True)
plt.show()

# ##### To generate how much gain and phase pargin this system have?
#
# gm, pm, _, _ = control.margin(sys)
#
# print("Gain Margin:", gm)
# print("Phase Margin:", pm)
#
# # # Calculate bandwidth
# bw = control.bandwidth(sys)
# print("Bandwidth:", bw)