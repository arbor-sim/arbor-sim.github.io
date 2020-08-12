---
layout: post
title:  "Release: Version 0.2"
---
**Arbor** library **version 0.2**, tagged as `v0.2`

Arbor is a library for implementing performance portable network simulations of multi-compartment neuron models.

An installation guide and library documentation are available online at [Read the Docs](https://arbor.readthedocs.io/en/latest/).

[Submit a ticket](https://github.com/eth-cscs/arbor) if you have any questions or want help.


Some key features include:

  * Optimized back ends for CUDA, KNL, AVX2, ARM NEON intrinsics.
  * Asynchronous spike exchange that overlaps compute and communication.
  * Efficient sampling of voltage and current on all back ends.
  * Efficient implementation of all features on GPU.
  * Reporting of memory and energy consumption (when available on platform).
  * An API for addition of new cell types, e.g. LIF and Poisson spike generators.

## Change Log

Changes since [v0.1](https://github.com/arbor-sim/arbor/releases/tag/v0.1):

  * A new Hines matrix solver back end for the GPU that parallelises over cell
    branches, not cells, to increase the amount of parallelism. See #631.
  * Support for describing and simulating electrical gap junctions. See #661 #686.
  * An additional library `libarborenv` is now installed with useful
    helper functionality for managing the environment (e.g. detecting the number of available CPU cores). See #679.
  * Detection and allocation of GPUs to MPI ranks on systems with more than one GPU per node in `libarborenv`. See #659 and #654.
  * The miniapp example was removed and replaced with a simple single cell model that shows how to use morphologies. See #703 and #710.
  * Support for ARM NEON intrinsics. See #698.
  * Basic Python support. Full Python support is slated for v0.3. See #668.

### Contributors

Nora Abi Akar
John Biddiscombe
Benjamin Cumming
Felix Huber
Marko Kabic
Vasileios Karakasis
Wouter Klijn
Anne Küsters
Alexander Peyser
Stuart Yates

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2583709.svg)](https://doi.org/10.5281/zenodo.2583709)

Nora Abi Akar, John Biddiscombe, Benjamin Cumming, Felix Huber, Marko Kabic, Vasileios Karakasis, Wouter Klijn, Anne Küsters, Alexander Peyser, Stuart Yates. (2019, March 4). arbor-sim/arbor: Arbor Library v0.2 (Version v0.2). Zenodo. http://doi.org/10.5281/zenodo.2583709
