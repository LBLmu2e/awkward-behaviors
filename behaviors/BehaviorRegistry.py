# Ed Callaghan
# Mu2e awkward behavior registry, with hook into awkward registry
# October 2024

import awkward as ak

class BehaviorRegistry(dict):
    def __init__(self, *args, **kwargs):
        super(BehaviorRegistry, self).__init__(*args, **kwargs)

    def Register(self, label, record_class, array_class):
        mapping = {
                    label  : record_class,
              ('*', label) : array_class,
        }
        self.update(mapping)
        ak.behavior.update(mapping)

    def __str__(self, *args, **kwargs):
        rv = super(BehaviorRegistry, self).__str__(*args, **kwargs)
        return rv

behaviors = BehaviorRegistry()
numerics = [
            'int',
            'float',
            'double',
]
coordinate_systems = [
]
coordinate_system_tags = [
    'ROOT::Math::DefaultCoordinateSystem',
]
