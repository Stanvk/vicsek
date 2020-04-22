from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class Animator2D:
    """
    Animator class for 2D graphical representation.
    """

    def __init__(self):
        """
        Constructor. Returns the Animator2D instance.
        """
        pass

    def prepareAnimation(self, figure, interval = 20, frames=100):
        """
        Prepares the 2D animator object for animation.

        keyword arguments:
        figure -- Matplotlibs figure object.
        interval -- The interval between two frames.
        frames -- The number of frames used in the animation.
        """
        self._figure = figure
        self._interval = interval
        self._frames = frames

        return self
  
    def feedSimulationData(self, simulationData, domainSize):
        """
        Gets the simulation data and domain size and saves them as class properties.

        keyword arguments:
        simulationData -- The simulation data array.
        domainSize -- The tuple that represents the lenghts of the square domain in each dimension.

        return:
        self
        """
        
        self._time, self._positions, self._orientations = simulationData
        self._domainSize = domainSize

        return self

    def showAnimation(self):
        """
        Executes the animation and shows it to the user.
        
        returns
        animation object
        """
        animation = FuncAnimation(self._figure, self._animate, interval=self._interval, frames = self._frames)
        plt.show()

        return animation

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
