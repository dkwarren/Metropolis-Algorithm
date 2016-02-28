# Final Project Metropolis Algorithm
# Gregor Ramien and David Warren II

import random
import matplotlib.pyplot as plt
import numpy as np

def make_particle(maxE):
    return int(random.randint(1,maxE))
    
def random_probability():
    return random.random()
    
def make_microstate(state, N, maxE):
    for x in range(0,N):
        state.append(make_particle(maxE))
        
def avgE(state, beta):
    avg_energy = 0
    for i in range(len(state)):
        avg_energy += state[i]*np.exp(-beta*float(state[i]))
    return avg_energy
    
def perturbation():
    return random.randrange(-1,1,2)
    
def random_particle(N):
    return random.randint(0,N-1)
    
def plot_energies(values, N):
    plt.figure(1)
    plt.plot(energy[0], 'g', energy[1], 'r', energy[2], 'b', energy[3], 'c', energy[4], 'm')
    plt.title("Average Energy Values vs. Microstates")
    plt.xlabel("Microstates " + str(N) + " Particles " + str(trials) + " trials")
    plt.ylabel("Average Energy")
    plt.show()

def plot_avg_energies(values, temp, analytic):
    plt.figure(2)
    plt.semilogx(temp, values)#, 'b', temp, analytic, 'r')
    plt.title("Average Energy vs. Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Average Energy(T)")
    plt.show()
    
def main(N, T, maxE, trials):
    state = []
    energy = []
    beta = float(1/T)
    
    make_microstate(state, N, maxE)     # Makes a microstate with N particles and a 
                                        # max energy of 1000
                                        
    energy.append(avgE(state,beta))      # Averages the energy of the microstate
    
    for x in range(trials):
        choice = random_particle(N)     # Random particle to perturb
        dE = perturbation()             # -1 or 1 energy change
        if state[choice] + dE >= 0.5:    # This checks that the energy value does
                                        # not go below the ground state 0.5
            if dE < 0:
                state[choice] = state[choice] + dE  # Accepts new microstate
            if dE > 0:
                r = random_probability()       # Generates random probability
                if r < np.exp(-beta*dE):   
                    state[choice] = state[choice] + dE     # Accepts new microstate
        energy.append(avgE(state, beta))
        
    return energy
    
###############################################################################            
N = 200
maxE = 50
trials = 10000
h = 1
w = 1
energy = []
avg = []
temprange = list(range(10,100))

for i in range(len(temprange)):
    energy.append(main(N, temprange[i], maxE, trials))
    beta = 1/float(temprange[i])
    avg.append(avgE(energy[i][-100::],beta))
    
analytic_energy = []

for i in temprange:
    analytic_energy.append(N*h*w*(0.5 + 1/(np.exp(h*w/float(i))-1)))
    
plot_energies(energy, N)
plot_avg_energies(avg, temprange, analytic_energy)

plt.figure(3)
plt.semilogx(temprange, analytic_energy)
plt.xlabel("Temperature")
plt.ylabel("Analytical Energy")
plt.title("Analytical Energy vs. Temperature")
plt.show()

deviation = []
for i in range(len(temprange)):
    deviation.append(avg[i] - analytic_energy[i])
plt.figure(4)
plt.plot(deviation)
plt.xlabel("Microstates")
plt.ylabel("Deviation")
plt.title("Deviation from Analytical Energy")
plt.show()
###############################################################################