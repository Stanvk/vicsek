import Vicsek
import matplotlib.pyplot as plt
import numpy as np

sim = Vicsek.Vicsek()
positions, orientations = sim.simulate()

plt.figure()

positions = np.array(positions)
orientations = np.array(orientations)

print(positions)

#for i in range(positions.shape[1]):
#    plt.scatter(positions[:,i,0], positions[:,i,1])

plt.scatter(positions[:,1,0],positions[:,1,1])

plt.show()
