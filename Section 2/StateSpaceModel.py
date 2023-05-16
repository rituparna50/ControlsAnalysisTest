# Section 2
# Part 1

        #Create aircarft state space model

import numpy as np

# Given values
V= 279.1    # ft/sec
rho = 0.002377  #slug/ft^3
S = 5500    # ft^2
c_bar = 27.3    # ft
W = 564,032     # lb
b = 195.7   # ft
Ix = 14.3e6  # slug ft^2
Iy = 32.3e6  # slug ft^2
Iz = 45.3e6  # slug ft^2
Ixz = -2.23e6  # slug ft^2

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

Conversion Factors
lbs_to_slug = 1 / 32.174    # Conversion from lb to slug
ft_to_m = 0.3048    # Conversion from ft to meters

# Constants
g = 32.174  # ft/sec^2

# Compute relevant parameters
m = (W * lbs_to_slug) / g   # Mass (slug)
Q = 0.5 * rho * V**2    # Dynamic Pressure (lb/ft^2)

# State vector x = [v
                #   p
                #   phi
                #   r]

# Control vector --> eta = [del_r
                        #   del_a]
#Sideslip angle beta


