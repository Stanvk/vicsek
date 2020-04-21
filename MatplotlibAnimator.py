import matplotlib.pyplt as plt

class MatplotlibAnimator:

    _simulationData = {}

    _figure

    _animator

    def __init__(self, simulationData = {}, domainSize):
        self._simulationData = simulationData
        self._domainSize = domainSize

        self._initialize()

    def prepare(self, animator):
        return animator.prepareAnimation(self._figure)

    def _initialize(self):
        self._figure = plt.figure()
        self._figure.clf();
        
        return self.figure
