# ControlsAnalysisTest

# Section 2

## Part 1 
Given values 
V = 279.1 ft/sec    // Velocity
rho = 0.002377 slug/ft^3    //Density
S = 5500 ft^2       // Wing span
c_bar = 27.3 ft     // mean chord length
W = 564032 lb     //Weight
b = 195.7 ft 
Iy = 32.3 * 10^6 slug ft^2  //Moment of inertia about y axis 
Ix = 14.3 * 10 ^6 slug ft^2
Iz = 45.3 * 10^6 slug ft^2 
Ixz = -2.23 * 10^6 slug ft^2
  
  Aerodynamic derivatives 
CyB = -0.96
Cyp = 0.0 
Cyr = 0.0

ClB = -0.221 
Clp = -0.45
Clr = 0.101

CnB = 0.15 
Cnp = -0.121
Cnr = -0.30

Y_sig_r = (Q*S*Cy_sig*r)/m

Created a lateral aircraft stat space model (A, B, C, D) matrices, using a state vector of x= [ v p phi r]^T and control vector Eta = [Sig_r Sig_a]^T

Showed a pole-zero map of the state-space plant and describe how each pole represents a lateral stability mode --
  -if there are zeroes, why there are zeroes 
  -Are any poles close to being unstable or are there anyunstable poles?
    - Is this concerning? 
   
  How does increasing dihedral change the spiral mode?
   - Which direction would you expect which pole to move, only related to the spiral mode
  
  Showed a step response of roll rate given an input 
  - Described the plot


# Section 3 

Not using any pre-existing library except for an ODE solver

## Part 1 
Created a simulation og a spring-mass-damper system implemented in Python. The result of the simulation outputs time, position, velocity as lists or a Pandas DataFrame stored in a csv. Use any ODE solver you like, you do not have to write one. 
Describe any parameter you choose and the justification for doing so. (e.g simulation time, timee step, mass, damping coefficient, spring coefficient)

## Part 2 -- 
Applied a PID controller to the spring-mass-damper system. Do not use a PID library, write one from scratch. 

## Part 3 -- 
Performed open-loop stability analysis on your system. What is the stability of the plant? Gain and phase margins? 
Found what is the open-loop stability of the entire syste, (Controller --> Plant)? Gain and phase margin?
Showed a step response of the plant, does this agree with your stability analysis and simulation?


