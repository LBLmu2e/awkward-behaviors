# Ed Callaghan
# Point in 3D space using cartesian coordinates
# October 2024

import awkward as ak
import numpy as np
from behaviors.BehaviorRegistry import behaviors, numerics

class ROOT_Math_Cartesian3D(ak.Record):
    def x(self):
        rv = self.fX
        return rv

    def y(self):
        rv = self.fY
        return rv

    def z(self):
        rv = self.fZ
        return rv

    def magnitude(self):
        rv = pow(pow(self.x(), 2) + pow(self.y(), 2) + pow(self.z(), 2), 0.5)
        return rv

    def rho(self):
        rv = pow(pow(self.x(), 2) + pow(self.y(), 2),0.5)
        return rv

    def cosTheta(self):
        rv = self.z()/self.magnitude()
        return rv

    def phi(self):
        rv = np.atan2(self.y(),self.x())
        return rv

RecordType = ROOT_Math_Cartesian3D
class ROOT_Math_Cartesian3D__Array(ak.Array):
    def x(self):
        rv = RecordType.x(self)
        return rv
    def y(self):
        rv = RecordType.y(self)
        return rv
    def z(self):
        rv = RecordType.z(self)
        return rv
    def magnitude(self):
        rv = RecordType.magnitude(self)
        return rv
    def rho(self):
        rv = RecordType.rho(self)
        return rv
    def cosTheta(self):
        rv = RecordType.cosTheta(self)
        return rv
    def phi(self):
        rv = RecordType.phi(self)
        return rv

template = 'ROOT::Math::Cartesian3D<%s>'
for numeric in numerics:
    label = template % numeric
    behaviors.Register(label, ROOT_Math_Cartesian3D, ROOT_Math_Cartesian3D__Array)
