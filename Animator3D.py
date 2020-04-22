import matplotlib.pyplot as plt
import Animator
from mpl_toolkits.mplot3d import Axes3D

class Animator3D(Animator.Animator):
    """
    Animator class for 3D graphical representation.
    """

    def __init__(self):
        """
        Constructor. Returns the Animator2D instance.
        """
        pass

    def _animate(self, i):
        """
        Animator class that goes through sim data.

        keyword arguments:
        i -- Loop index.
        """
        plt.clf()
        ax = Axes3D(self._figure)
        plt.quiver(self._positions[i,:,0],self._positions[i,:,1],self._positions[i,:,2],self._orientations[i,:,0],self._orientations[i,:,1],self._orientations[i,:,2])
        plt.xlim(0,self._domainSize[0])
        plt.ylim(0,self._domainSize[1])
        ax.set_zlim(0,self._domainSize[2])
        ax.view_init(azim=(0.25*i % 360))
        plt.title('$t$=%2.2f' % self._time[i]) 
