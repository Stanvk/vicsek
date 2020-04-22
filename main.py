import Vicsek
import matplotlib.pyplot as plt
import matplotlib.animation as animator
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

sim = Vicsek.Vicsek(domainSize=(50,50), numberOfParticles=300)
time, positions, orientations = sim.simulate()

def animate_2D(time,positions,orientations, show=True):
    fig = plt.figure()
    
    def animate(i):
        plt.clf()
        plt.quiver(positions[i,:,0],positions[i,:,1],orientations[i,:,0],orientations[i,:,1])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        plt.title('$t$=%2.2f' % time[i])
    
    anim = FuncAnimation(fig, animate, interval=20, frames = len(time))
    
    if show:
        plt.show()
    
    return anim

def animate_3D(time, positions, orientations, show=True):
    fig = plt.figure()

    def animate(i):
        plt.clf()
        ax = Axes3D(fig)
        plt.quiver(positions[i,:,0],positions[i,:,1],positions[i,:,2],orientations[i,:,0],orientations[i,:,1],orientations[i,:,2])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        ax.set_zlim(0,sim.domainSize[2])
        ax.view_init(azim=(0.25*i % 360))
        plt.title('$t$=%2.2f' % time[i])


    anim = FuncAnimation(fig, animate, interval=20, frames=len(time))
    
    if show:
        plt.show()

    return anim

def save_animation(anim):
    FFwriter = animator.FFMpegWriter(fps=25, codec="h264")     
    anim.save('vicsek.mp4', writer = FFwriter )

anim = animate_2D(time,positions,orientations)

#save_animation(anim)
