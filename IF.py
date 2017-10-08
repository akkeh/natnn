import numpy as np
import matplotlib.pyplot as plt
''' ----------------------------------------------------------------- ***
    Integrate and fire                                                 |
        - Ohmic leakage current + voltage gated currents deactivated   |
            at rest                                                    |
            CV' = I - gleak(V - Eleak)                                 |
                if V == Ethresh: activation of volrage-sensitive       |
                    currents -> action potential, V <- Ek              |
    References:                                                        |
        Izhikevich, E.M. (2007)                                        |
*** ----------------------------------------------------------------- '''
class passive_IF:
    C = 1.0     # capacitance
    V0 = -70    # reset V
    El = -60    # leak equilibrium potential
    Eth = -55   # spike treshold
    g = 0.001   # conductance
    
    V = 0.0     # membrane potential

    def simulate(self, I):
        Vs = np.zeros(len(I))
        spikes = []
        for n in range(len(I)):
            dV = (I[n] - self.g*(self.V - self.El)) / self.C
            V = self.V + dV
            if V >= self.Eth:
                V = self.V0
                spikes.append(n)
            self.V = V
            Vs[n] = V
        return Vs, spikes

    def __init__(self, V0=-70, El=-60, Eth=-55, g=0.001):
        self.V0 = V0
        self.El = El
        self.Eth = Eth
        self.g = g


