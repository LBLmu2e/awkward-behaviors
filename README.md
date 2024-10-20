# awkward-behaviors
Abstract high-level functionality on Mu2e ntuple data structures using awkward behaviors.

A behavior can be defined on any composite type following the pattern exhibited by Mu2eTrkFitInfo and the ROOT examples, namely:
    1. Assume that all data members of the type are available
    2. Subclass awkward.Record and define methods which implement the high-level functionality
    3. Subclass awkward.Array and defer the same functionality to the previously-defined record subclass
    4. Register the record and array subclasses with the type name, after any typedefs and template specializations
