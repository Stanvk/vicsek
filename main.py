import Vicsek
import matplotlib.pyplot as plt

sim = Vicsek.Vicsek()
time, positions, orientations = sim.simulate()

plt.figure()

for i in range(positions.shape[1]):
    plt.scatter(positions[:,i,0], positions[:,i,1])


plt.show()
