class 2DAnimator:

    _figure

    _interval

    _frames

    def __init__(self):

    def prepareAnimation(self, figure, interval = 20, frames=100):
        self._figure = figure
        self._interval = interval
        self._frames = frames

        return self
   
    def showAnimation(self)
        animation = FuncAnimation(self._figure, self._animate, interval=self._interval, frames = self._frames)
        plt.show()

        return animation

    def _animate(self, figure):
        plt.quiver(positions[i,:,0],positions[i,:,1],orientations[i,:,0],orientations[i,:,1])
        plt.xlim(0,sim.domainSize[0])
        plt.ylim(0,sim.domainSize[1])
        plt.title('$t$=%2.2f' % time[i])
