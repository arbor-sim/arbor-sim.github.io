---
layout: page
frontpage: true
title: Home
---
# What is Arbor?

Arbor is a performance portable library for simulation of large networks of multi-compartment neurons on contemporary high-performance computing (HPC) systems. It is specialized for graphics processing units (GPUs), vectorized multicore, Intel KNL and laptops with a modular design for extensibility to new computer architectures.

## What's it good for?

Arbor is designed to handle very large, very long and computationally intensive problems in neuroscience. Further, Arbor aims to prepare neuroscience users for new HPC architectures. At the same time, Arbor is meant to be easy to use and understand, so that also beginners to computational neuroscience can get up to speed quickly. Whether your model is large or small, Arbor is able to compute your result on almost any hardware as quick as possible.

## Where is it used?

Arbor models multi-compartment neurons characterized by axonal delays, synaptic functions and cables. Besides multi-compartment cells Arbor also models leaky integrate-and-fire cells and artificial spike sources.

## Use cases?

Use cases have included the neocortical simulations, macaque visual cortical areas, and olfactory bulb simulations. Arbor developers are collaborating with researchers and modellers in the development of efficient support for structural plasticity.

## Who uses it?

Arbor applications have so far been focused primarily on synthetic verification, testing and performance benchmarks (see <https://arxiv.org/abs/1901.07454> for details).

However, it is planned to increase the user base within the next three years by preparing user-defined cellular-level models for portable HPC simulations using Arbor across a variety of current and emerging supercomputing resources through a Call for Expression of Interest (check out <https://www.humanbrainproject.eu/en/collaborate/open-calls/> for updates).

Expert computational neuroscientists from both outside and inside the Human Brain Project (HBP) are invited to develop models and adapt workflows for Arbor, specifically for networks of detailed cell models that require HPC (<https://github.com/arbor-sim/arbor>).

## Where do I get it?

Arbor is developed by the Swiss National Supercomputing Center and the Jülich Supercomputing Center under the auspices of the HBP as an active open source project, developed using an open-development model with code, continuous integration, bug reports and issues hosted on GitHub: <https://github.com/arbor-sim/arbor>. Benchmarking and validation of Arbor and other simulators can be performed with the NSuite performance and validation testing suite (<https://nsuite.readthedocs.io>, <https://github.com/arbor-sim/nsuite>).

## Is it suitable for me?

Use Arbor if you have the need to run your detailed cellular-level model in an efficient manner; Arbor has been designed to become an order of magnitude more efficient both in terms of solution times and memory usage as compared to existing simulation engines, without sacrificing ease of use and flexibility (see <https://arxiv.org/abs/1901.07454> for details). Full support for the SONATA model exchange format is under active development, and Arbor will also provide APIs for integration with other tools and simulators, including co-simulation with NEST (<https://www.nest-simulator.org>) mediated via spike exchange for large, multi-scale brain simulations, and participation in orchestrated simulation, analysis and visualization applications with NEST, Elephant (<http://neuralensemble.org/elephant/>), TVB (<https://www.thevirtualbrain.org>) and other tools using the HBP in-situ pipeline (<https://hbp-hpc-platform.fz-juelich.de/?hbp_software=in-situ-pipeline>).

## How do I work with it?

Arbor provides both a low level C++ API and a higher level Python API:

-   The Python API is expected to be the most commonly used interface for computational neuroscientists 
    (visit <https://arbor.readthedocs.io/en/latest/py_intro.html> for more details).

-   The C++ API provides full control over Arbor simulations, and may be required for tightly integrated simulations
    or scenarios where efficiency at scale is paramount (visit <https://arbor.readthedocs.io/en/latest/cpp_intro.html>
    for more details).

__________________________________________________________
