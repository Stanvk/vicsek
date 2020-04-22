from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class Animator(object):
    
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
        self._animation = FuncAnimation(self._figure, self._animate, interval=self._interval, frames = self._frames)
        plt.show()

        return self

 
