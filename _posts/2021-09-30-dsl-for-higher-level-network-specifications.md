---
layout: post
title: "DSL for higher level network specifications"
categories: projects
tags: projects
---

We aim to design a high-level, declarative specification of network connectivity
for use in simulations of morphologically detailed neurons [1]. Many simulators and
network data formats use lists of 1:1 connections to describe and instantiate
networks. Sometimes features exist to describe randomized connections and
parameters in these connectivity descriptions. We seek to formulate and implement
a domain-specific language (DSL), informed by prior art [2,3,4], that can describe
such higher level connectivity. The project includes a study of the design space
simulators and the requirements of neuroscientists. From this a model should be
developed that captures practical users' needs while building upon a composable
structure. The end result is inclusion of this network DSL in Arbor [1], and
and perhaps eventual (partial) inclusion in other formats [4].

1. https://github.com/arbor-sim/arbor/issues/418
2. https://www.ncbi.nlm.nih.gov/pubmed/22437992
3. https://www.neuroml.org/
4. https://github.com/NeuroML/NeuroMLlite/
5. https://github.com/arbor-sim/arbor

We are estimating this to be a 6-12 month project, suitable for a Master student
looking for a thesis-project, or with a optionally increased scope suitable as a side-project for a PhD student or Postdoc with some prior experience. Depending on
the candidate and available time we could change the scope as needed. A background in
neuroscience, especially in modeling, and experience with other simulation tools 
is helpful. We require a working knowledge of C++.

If you are interested, please [get in touch](mailto:contact@arbor-sim.org).
