import matplotlib.pyplot as plt

class MatplotlibAnimator:
"""
The animator instance driven by Matplotlib.
"""
    
    def __init__(self, simulationData, domainSize):
        """
        Constructor.

        keyword arguments:
        simulationData -- The simulation data array.
        domainSize -- The tuple that represents the lenghts of the square domain in each dimension.
        """
        self._simulationData = simulationData
        self._domainSize = domainSize

        self._initialize()

    def prepare(self, animator):
        """
        Prepares the appropriate animator.

        keyword arguments:
        animator -- The appropriate animator class.

        return:
        Prepared animator feeded with simulation data.
        """
        preparedAnimator =  animator.prepareAnimation(self._figure)

        return preparedAnimator.feedSimulationData(self._simulationData, self._domainSize)

    def _initialize(self):
        """
        Initializes matplotlib for animation.
        
        return:
        plt.figure()
        """
        self._figure = plt.figure()
        
        return self._figure
