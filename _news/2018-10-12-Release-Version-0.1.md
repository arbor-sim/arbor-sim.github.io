---
layout: post
title:  "Release: Version 0.1"
---
# Arbor Library

**Arbor** library **version 0.1**, tagged as `v0.1`

Arbor is a library for implementing performance portable network simulations of multi-compartment neuron models.

An installation guide and library documentation are available online at [Read the Docs](http://arbor.readthedocs.io/en/v0.1/).

[Submit a ticket](https://github.com/eth-cscs/arbor) if you have any questions or want help.


Some key features include:

    * Optimized back ends for CUDA, KNL and AVX2 intrinsics.
    * Asynchronous spike exchange that overlaps compute and communication.
    * Efficient sampling of voltage and current on all back ends.
    * Efficient implementation of all features on GPU.
    * Reporting of memory and energy consumption (when available on platform).
    * An API for addition of new cell types, e.g. LIF and Poisson spike generators.
    * Validation tests against numeric/analytic models and NEURON.

### Contributors
Nora Abi Akar
John Biddiscombe
Benjamin Cumming
Marko Kabic
Vasileios Karakasis
Wouter Klijn
Anne Küsters
Ivan Martinez
Alexander Peyser
Stuart Yates

## Citation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1459679.svg)](https://doi.org/10.5281/zenodo.1459679)

If you use this version of Arbor, please cite it as **Nora Abi Akar, John Biddiscombe, Benjamin Cumming, Marko Kabic, Vasileios Karakasis, Wouter Klijn, Anne Küsters, Ivan Martinez, Alexander Peyser, Stuart Yates. (2018, October 12). arbor-sim/arbor: Version 0.1: First release (Version v0.1). Zenodo. http://doi.org/10.5281/zenodo.1459679**. The full citation is available in different formats on [Zenodo]( http://doi.org/10.5281/zenodo.1459679).
