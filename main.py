import Vicsek
import matplotlib.pyplot as plt
import matplotlib.animation as animator
from matplotlib.animation import FuncAnimation

sim = Vicsek.Vicsek(domainSize=[100,100,100], numberOfParticles=600)
time, positions, orientations = sim.simulate()

def animate_2D(time,positions,orientations):
    fig = plt.figure()
    
    def animate(i):
        plt.clf()
        plt.quiver(positions[i,:,0],positions[i,:,1],orientations[i,:,0],orientations[i,:,1])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        plt.title('$t$=%2.2f' % time[i])
    
    anim = FuncAnimation(fig, animate, interval=20, frames = len(time))
    
    return anim

def animate_3D(time, positions, orientations):
    fig = plt.figure()

    def animate(i):
        plt.clf()
        ax = fig.gca(projection='3d')
        plt.quiver(positions[i,:,0],positions[i,:,1],positions[i,:,2],orientations[i,:,0],orientations[i,:,1],orientations[i,:,2])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        ax.set_zlim(0,sim.domainSize[2])
        plt.title('$t$=%2.2f' % time[i])


    anim = FuncAnimation(fig, animate, interval=20, frames=len(time))

    return anim

anim = animate_3D(time,positions,orientations)

FFwriter = animator.FFMpegWriter(fps=50, codec="h264")     

anim.save('vicsek.mp4', writer = FFwriter )

