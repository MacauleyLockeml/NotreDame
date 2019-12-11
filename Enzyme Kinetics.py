import numpy as np
import matplotlib as plt
import random
import math

#Storage Array for population time

# Substrate, Enzyme, Complex, Product
pop=[1000,100,0,0]

#Constants

k1=1.1 # bindings per minute (Rate of Complex Formation)
kminus1=0.9 # dissociations per minute (Rate of Complex Dissociation)
k2=0.6 #products formed per minute (rate of Product formation)

#Perform a Gillespie Simulation

#set initial time to 0
t=0

while pop[0]>0:

    #Define rates of each reaction

    Complex_formed=k1*pop[0]*pop[1]
    Complex_dissociates=kminus1*pop[2]
    product_formed=k2*pop[2]

    #define total propensity (sum of all rates)

    alpha_0=Complex_formed+Complex_dissociates+product_formed

    #Draw a time step from the exponential distribution

    delta_t=-math.log(random.uniform(0,1))/alpha_0
    t=t+delta_t #update time

    #Draw a random number from the uniform distribution 

    u2=random.uniform(0,1)

    #Pick a reaction and update population

    if u2<Complex_formed/alpha_0:
        pop[0]=pop[0]-1  #loss of one substrate
        pop[1]=pop[1]-1  #loss of one free enzyme
        pop[2]=pop[2]+1  #complex formed

    elif u2<(Complex_formed+Complex_dissociates)/alpha_0:
        pop[0]=pop[0]+1 #one substrate released from complex
        pop[1]=pop[1]+1 #one enzyme released from complex
        pop[2]=pop[2]-1 #lose one complex

    else:
        pop[1]=pop[1]+1 #One enzyme released
        pop[2]=pop[2]-1 #One complex lost
        pop[3]=pop[3]+1 #One product formed 

    print(pop)

#end of Simulation when while loop ends
print(pop)

