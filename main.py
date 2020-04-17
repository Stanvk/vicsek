import Vicsek
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sim = Vicsek.Vicsek()
time, positions, orientations = sim.simulate()

plt.figure()

for i in range(positions.shape[1]):
    plt.scatter(positions[:,i,0], positions[:,i,1])

xcor = positions[:,:,0]
ycor = positions[:,:,1]

t = xcor.shape[0]

fig, ax = plt.subplots(figsize=(5,3))
ax.set(xlim=(0,100), ylim=(0,100))
scat = ax.scatter(xcor[0, :],ycor[0,:])

#line = ax.plot(x, F[0,:], color='k', lw=2)[0]

def animate(i):
    scat.set_offsets(np.c_[
        xcor[i,:],
        ycor[i,:]
    ])

anim = FuncAnimation(fig, animate, interval=100, frames = t-1)

plt.draw()
plt.show()

