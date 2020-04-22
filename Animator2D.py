import matplotlib.pyplot as plt
import Animator

class Animator2D(Animator.Animator):
    """
    Animator class for 2D graphical representation.
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
        plt.quiver(self._positions[i,:,0],self._positions[i,:,1],self._orientations[i,:,0],self._orientations[i,:,1])
        plt.xlim(0,self._domainSize[0])
        plt.ylim(0,self._domainSize[1])
        plt.title('$t$=%2.2f' % self._time[i])
