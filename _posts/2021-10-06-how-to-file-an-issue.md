---
layout: post
title: How to file an Issue?
---

As of today we have a improved our Github Issue templates slightly. They'll show when you file one at <https://github.com/arbor-sim/arbor/issues/new/choose>.

Issues are not just for bugs, we use them also for Feature Requests. An example feature you want Arbor to have is file format X support. You want this feature because you have found a fantastic model of something you're writing a publication on in model database Y. Model database Y makes their stuff available in format X, hence you needing this feature. You want this feature rather quickly, because you have a submission deadline in 3 months! How do you file that issue?

The Feature Request Issue is pre-filled with the following template:

    **Describe the feature you need**
    <!-- Example: I want Arbor to support file format X -->

    **Explain what it is supposed to enable**
    <!-- Example: Model database Y can export in format X, which means I could use their models in Arbor. -->

    **Additional context**
    <!-- Example: I'm writing a paper on the olfactory bulb and database Y has a model ready to go! -->

There's a few sections here with the above example pre-filled in HTML comment tags (you can replace that with your actual issue). Try to make this description elaborate enough such that others can understand the _what_ and the _why_, and what, if anything, you have tried in terms of _how_. Don't worry if you've not tried anything; the idea of a Feature Request is not that you're on the hook for writing the code that will address it. Rather, the idea is that you together with others will find a good approach for an implementation before too much time is spent on writing one that possibly needs to be discarded, because it turns out that someone else knew of an important reason or edge-case why that particular implementation would never work. The Feature Request is meant to communicate your need, and a signal for all Arborians to sit down and cooperate on the best solution for that need.

When you file an Issue, and a Feature Request in particular, make sure you add or remove relevant labels, which help others roughly understand what the request pertains to. There are also two priority labels, which you can use to signal your urgency and desire for a timeline on addressing the issue. Although we try to have timely replies to all Issues, those labelled with a priority will get, you guessed right, priority.

Happy [filing](https://github.com/arbor-sim/arbor/issues/new/choose)!
