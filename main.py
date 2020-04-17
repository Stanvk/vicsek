import Vicsek
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sim = Vicsek.Vicsek()
time, positions, orientations = sim.simulate()

def animate_2D(time,positions,orientations):
    fig=plt.figure()
    
    def animate(i):
        plt.clf()
        plt.quiver(positions[i,:,0],positions[i,:,1],orientations[i,:,0],orientations[i,:,1])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        plt.title('$t$=%2.2f' % time[i])
    
    anim = FuncAnimation(fig, animate, interval=20, frames = len(time))
    
    plt.show()

animate_2D(time,positions,orientations)