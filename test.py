import Vicsek
import MatplotlibAnimator
import Animator2D

simulator = Vicsek.Vicsek(domainSize=(50,50), numberOfParticles=300)
simulationData = simulator.simulate()

"""
Initialize the Matplotanimator and feed the simulation data and domain size.
"""
animator = MatplotlibAnimator.MatplotlibAnimator(simulationData, (50,50))

"""
Prepare the animator for a 2D representation.
"""
preparedAnimator = animator.prepare(Animator2D.Animator2D())

"""
Execute and show the animation.
"""
preparedAnimator.showAnimation()
