import Vicsek
import MatplotlibAnimator
import Animator2D
import Animator3D

simulator = Vicsek.Vicsek(domainSize=(50,50,50), numberOfParticles=100)
simulationData = simulator.simulate()

"""
Initialize the Matplotanimator and feed the simulation data and domain size.
"""
animator = MatplotlibAnimator.MatplotlibAnimator(simulationData, (50,50,50))

"""
Prepare the animator for a 2D representation.
"""
preparedAnimator = animator.prepare(Animator3D.Animator3D())

"""
Execute and save the animation as an mp4.
"""
preparedAnimator.saveAnimation('vicsek2.mp4')

"""
After saving the animation we can also show it directly.
"""
preparedAnimator.showAnimation()
