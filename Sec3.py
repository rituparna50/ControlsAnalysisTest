#Simulation of spring-mass-damper system
import pandas as pd
from scipy.integrate import odeint

## Part 1 - Create a simulation og a spring-mass-damper system implemented in Python. The result of the simulation outputs time, position, velocity as lists or a Pandas DataFrame stored in a csv. Use any ODE solver you like, you do not have to write one. Describe any parameter you choose and the justification for doing so. (e.g simulation time, timee step, mass, damping coefficient, spring coefficient)

from Functions import spring_mass_damper

#Initial conditions
x0 = 1.0    # Setting initial position in meters
v0 = 0.0    # Setting initial velocity in m/s
state0 = [x0, v0]

#Time points to evaluate the system
t = pd.Series([i *0.1 for i in range(100)])

#Solve for ODE using scipy's "odeint" ODE solver and the imported function
state = odeint(spring_mass_damper, state0, t)
position = state[:, 0]
velocity = state[:, 1]

results = pd.DataFrame({"Time":t, "Position":position, "Velocity":velocity})
#Create a Pandas dataframe to store the simulation results

#Specify directory path
directory_path = r'C:\Users\ritup\OneDrive\Documents\GitHub\ControlsAnalysisTest\Data\Sec3'

#Create the full path including directory and filename
file_path = directory_path + '\\spring_simulation.csv'

results.to_csv(file_path, index=False)
#Saving results to a CSV file


## -----------------------------------------------------

# PART 2
## Apply a PID controller to the spring-mass-damper system. Do not use a PID library, write one from scratch.

from Functions import pid_cntrl, spring_mass_damper_with_PID
# Calling two separate functions from Functions.py

# Giving values to PID Controller parameters
Kp = 1.0
Ki = 0.5
Kd = 0.2

#Initial conditions
x0 = 1.0    # Setting initial position in meters
v0 = 0.0    # Setting initial velocity in m/s
state0 = [x0, v0]

#Time points to evaluate the system
t = pd.Series([i *0.1 for i in range(100)])

prev_err = 0.0
err_integral = 0.0
dt = 0.1

#setting desired position for PID controller
des_pos = 0.0

#Solve for ODE using scipy's "odeint" ODE solver and the imported function
state = odeint(spring_mass_damper_with_PID, state0, t, args=(prev_err, err_integral, Kp, Ki,Kd, dt),)

positionPID = state[:, 0]
velocityPID = state[:, 1]

# Compute the PID controls signal for each time step
errs = [] #Initialize the list of errors
cntrl_signls = []  #Initialize the list of control signals

for i in range (len(t)):
    curr_err = des_pos - positionPID[i]
    cntrl_signl, err_integral = pid_cntrl (curr_err, prev_err, err_integral, Kp, Ki, Kd, dt)

    cntrl_signls.append(cntrl_signl)
    errs.append(curr_err)
    prev_err = curr_err

#Create a new dataframe for storing output obtained after using PID controller

resultsPID = pd.DataFrame({"Time":t, 'Position with PID':positionPID, 'Velocity with PID':velocityPID, 'Control signals':cntrl_signls, 'Error':errs})
#Create a Pandas dataframe to store the simulation results

#Specify directory path
directory_path = r'C:\Users\ritup\OneDrive\Documents\GitHub\ControlsAnalysisTest\Data\Sec3'

#Create the full path including directory and filename
file_path = directory_path + '\\spring_simulationPID.csv'

#Save the output to the specified file path
resultsPID.to_csv(file_path, index=False)

#####------------------------------------------------------------------

#PART 3
# To perform open loop stability analysis and demonstrate the step response of the syetm, we can use the control system analysis and simulation libraries from Python.
# These are the Control System Library (scipy.signal) and Control library (control)

import numpy as np
from scipy import signal

# Define the transfer function of the plant (spring-mass-damper system)
m = 1.0     # Mass in kg
k = 2.0     # Spring constant (N/m)
c = 0.5     # Damping coefficient (Ns/m)

num = [0, 0, 1]      # Numerator coefficients of the transfer function
den = [m, c, k]      # Denominator coefficients of the transfer function

plant_tf = signal.TransferFunction(num, den)

# Perform stability analysis
poles = plant_tf.poles
print("Poles are-", poles)

# Check if all poles have negative real parts
if np.all(np.real(poles) < 0):
    print("The plant is stable.")
else:
    print("The plant is unstable.")

