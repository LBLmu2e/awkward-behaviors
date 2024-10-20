# Ed Callaghan
# Vector in 3D Euclidean space using cartesian coordinates
# October 2024

import awkward as ak
from behaviors.BehaviorRegistry import behaviors, numerics, coordinate_system_tags
from behaviors.ROOT_Math_Cartesian3D import ROOT_Math_Cartesian3D

class ROOT_Math_XYZVector(ak.Record):
    def x(self):
        rv = self.fCoordinates.x()
        return rv

    def y(self):
        rv = self.fCoordinates.y()
        return rv

    def z(self):
        rv = self.fCoordinates.z()
        return rv

    def magnitude(self):
        rv = ROOT_Math_Cartesian3D.magnitude(self)
        return rv

RecordType = ROOT_Math_XYZVector
class ROOT_Math_XYZVector__Array(ak.Array):
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

template = 'ROOT::Math::DisplacementVector3D<'  \
         + 'ROOT::Math::Cartesian3D<%s>'        \
         + ','                                  \
         + 'ROOT::Math::DefaultCoordinateSystemTag>'
for numeric in numerics:
    label = template % numeric
    behaviors.Register(label, ROOT_Math_XYZVector, ROOT_Math_XYZVector__Array)
