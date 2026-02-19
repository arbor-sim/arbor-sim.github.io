---
layout: post
title: "Plastic Arbor: A modern simulation framework for synaptic plasticity—From single synapses to networks of morphological neurons"
---

# Plastic Arbor: A modern simulation framework for synaptic plasticity—From single synapses to networks of morphological neurons

[Article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013926)

From the abstract: 

Arbor is a software library designed for efficient simulation of large-scale
networks of biological neurons with detailed morphological structures. It
combines customizable neuronal and synaptic mechanisms with high-performance
computing, supporting multi-core CPU and GPU systems. In humans and other
animals, synaptic plasticity processes play a vital role in cognitive functions,
including learning and memory. Recent studies have shown that intracellular
molecular processes in dendrites significantly influence single-neuron dynamics.
However, for understanding how the complex interplay between dendrites and
synaptic processes influences network dynamics, computational modeling is
required. To enable the modeling of large-scale networks of morphologically
detailed neurons with diverse plasticity processes, we have extended the Arbor
library to support simulations of a large variety of spike-driven plasticity
paradigms. To showcase the features of the extended framework, we present
examples of computational models, beginning with single-synapse dynamics,
progressing to multi-synapse rules, and finally scaling up to large recurrent
networks. While cross-validating our implementations by comparison with other
simulators, we show that Arbor allows simulating plastic networks of
multi-compartment neurons at nearly no additional cost in runtime compared to
point-neuron simulations. In addition, we demonstrate that Arbor is highly
efficient in terms of runtime and memory use as compared to other simulators.
Using the extended framework, as an example, we investigate the impact of
dendritic structures on network dynamics across a timescale of several hours,
finding a relation between the length of dendritic trees and the ability of the
network to efficiently store information. By our extension of Arbor, we aim to
provide a valuable tool that will support future studies on the impact of
synaptic plasticity, especially, in conjunction with neuronal morphology, in
large networks.
