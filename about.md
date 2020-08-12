---
layout: page
title: About
---
# About Arbor

Arbor is a high-performance library for computational neuroscience simulations, being developed in work package 7.5.4 of the [Human Brain Project](//www.humanbrainproject.eu).

The development team is based in:

* [Swiss National Supercomputing Center](//www.cscs.ch) (CSCS)
* [Jülich Supercomputing Centre](//www.fz-juelich.de/ias/jsc/EN/) (JSC)

Arbor is designed from the ground up for **many core** architectures:

* Written in C++11 and CUDA;
* Distributed parallelism using MPI;
* Multithreading with TBB and C++11 threads;
* **Open source** and **open development**;
* Sound development practices: **unit testing**, **continuous Integration**, and **validation**.

We are actively [developing Arbor](//github.com/arbor-sim/arbor), improving performance and adding features. Some key features include:

* Optimized back end for CUDA
* Optimized vector back ends for Intel (KNL, AVX, AVX2) and Arm (ARMv8-A NEON) intrinsics.
* Asynchronous spike exchange that overlaps compute and communication.
* Efficient sampling of voltage and current on all back ends.
* Efficient implementation of all features on GPU.
* Reporting of memory and energy consumption (when available on platform).
* An API for addition of new cell types, e.g. LIF and Poisson spike generators.
* Validation tests against numeric/analytic models and NEURON.

