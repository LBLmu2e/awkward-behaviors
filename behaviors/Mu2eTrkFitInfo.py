# Ed Callaghan
# Fit sampled at a point
# October 2024

import awkward as ak
from behaviors.BehaviorRegistry import behaviors

class Mu2eTrkFitInfo(ak.Record):
    def momentum(self):
        rv = self.mom
        return rv

    def position(self):
        rv = self.pos
        return rv

    def momentum_uncertainty(self):
        rv =  self.momerr
        return rv

    def surface_id(self):
        rv = self.sid
        return rv

    def surface_index(self):
        rv = self.sindex
        return rv

RecordType = Mu2eTrkFitInfo
class Mu2eTrkFitInfo__Array(ak.Array):
    def momentum(self):
        rv = RecordType.momentum(self)
        return rv

    def position(self):
        rv = RecordType.position(self)
        return rv

    def momentum_uncertainty(self):
        rv = RecordType.momentum_uncertainty(self)
        return rv

    def surface_id(self):
        rv = RecordType.surface_id(self)
        return rv

    def surface_index(self):
        rv = RecordType.surface_index(self)
        return rv

label = 'mu2e::TrkFitInfo'
behaviors.Register(label, Mu2eTrkFitInfo, Mu2eTrkFitInfo__Array)
