---
layout: post
title:  "Release: Version 0.4"
---

**Arbor** library **version 0.4**, tagged as `[v0.4](https://github.com/arbor-sim/arbor/releases/tag/v0.4)`

## Release notes

### Library
* Moved from C++14 to C++17
    * Removed our hand-rolled versions of `any`, `optional` and `variant`.
* Added `std::expected` equivalent for error handling.

### Features
* Added mechanism catalogues with mechanisms used by Allen and BBP models.
* Removed support for spherical segments at the root of cable morphologies, and
  replaced the sample-based representation with a segment-based representation:
    * Morphologies are defined in terms of two-point segments.
    * Gaps are allowed between segments anywhere in a morphology.
* Exposed the current `time` inside mechanisms.
* Added support for NeuroML2 morphology descriptions.
* Added a "stitch" morphology builder for constructing morphologies with
  cable sections that can connect to any location on their parent cable.                    
* Replaced recipe probe API with more flexible API that allows for sampling
  not only voltages at single locations, but currents, ion species properties,
  and mechanism state variables at single locations or across an entire cell.
* Added support for querying probe metadata from the simulation object.
* Added new 'place_pwlin' C++ API for cell geometry queries.
* Added support for loading Allen SDK cell model morphologies from SWC.
* Added support for composing policies for creating compartments over sub-regions.

### Documentation
* Restructured documentation to have cleaner separation between high level descriptions
  of concepts and the C++ and Python APIs.
* Added high level documentation for morphology descriptions, labels and cable cell
  construction.

### Optimizations
* Implemented memory optimizations for GPU matrix solver.
* Added support for ARM SVE intrinsics in the vectorized CPU back end.

### Bug Fixes
* Fixed various modcc code generation errors.
