from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.animation as animator

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

    def saveAnimation(self, filename, fpsVar=25, codecVar="h264"):
        """
        Saves the animation.

        returns
        Animator
        """
        animation = self._generateAnimation();
        FFWriter = animator.FFMpegWriter(fps=fpsVar, codec=codecVar)
        animation.save(filename, writer=FFWriter)

        return self

    def showAnimation(self):
        """
        Show the animation to the user.

        returns
        self
        """
        animation = self._generateAnimation();
        
        plt.show()

        return self

    def _generateAnimation(self):
        """
        Generate the animation.
        
        returns
        animation object
        """
        self._animation = FuncAnimation(self._figure, self._animate, interval=self._interval, frames = self._frames)

        return self._animation

 
