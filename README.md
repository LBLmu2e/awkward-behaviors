# awkward-behaviors
Abstract high-level functionality on Mu2e ntuple data structures using awkward behaviors.

A behavior can be defined on any composite type following the pattern exhibited by Mu2eTrkFitInfo and the ROOT examples, namely:
    - Assume that all data members of the type are available
    - Subclass awkward.Record and define methods which implement the high-level functionality
    - Subclass awkward.Array and defer the same functionality to the previously-defined record subclass
    - Register the record and array subclasses with the type name, after any typedefs and template specializations
