#Defining the Spring-Mass-Damper function that will be used in the individual parts of this section

def spring_mass_damper(state, t):

    #Function to compute the derivatives of the state vector for a spring-mass-damper system
    #Arguments :

        #state -- list or array like, the state vector containing the position and velocity [x, v]
        # t -- float type, the time at which to evaluate the derivatives

    #Returns :
        #derivatives -- list, the computed derivatives [dx/dt, dv/dt]

    #Defining system parameters
    m = 1.0     #Mass in kg
    k = 2.0     # Spring constant (N/m)
    c = 0.5     # Damping coefficient (Ns/m)

    x, v = state    #Unpack state vector

    #Calculating the derivatives of the state vector
    dxdt = v
    dvdt = (1.0/m) * (-k * x - c * v)

    return [dxdt, dvdt]


def pid_cntrl(curr_err, prev_err, err_integral, Kp, Ki, Kd, dt):
## To compute the PID control signal based on the current error and controller parameters
# Arguments in pid_cntrl function

# curr_err -- Current error (difference between setpoint and actual value)
# prev_err -- Previous error before time step
# err_integral -- Total cumulative error
# Kp - Proportional gain
# Ki - Integral Gain
# Kd - Derivative Gain
# dt - Duration of a time step

## Returns of the function
#control -- PID control signal
#err_integral - Updated cumulative error

