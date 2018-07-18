ICML, Day 1: Tutorials

The first day of ICML consisted of a full day of tutorial sessions, for a full list see [ICML Schedule](https://icml.cc/Conferences/2018/Schedule?type=Tutorial). 
For the morning session, I decided to attend [Learning With Temporal Point Processes](http://learning.mpi-sws.org/tpp-icml18/):

Temporal point processes start from the observation that most time series are noisy observations of complex processes, observed asynchronously and at irregularly sampled intervals. In practice, a commonly used workaround to this is aggragating observations over an interval, but this leads to questions like how long the interval should be, how to handle intervals with 0 observations and so on.

Some applications outside finance are information propagation in socail networks or modelling infectious disease propagations.

Definition: A *temporal point process* is a random process whose realization consists of discrete events localized in time.

Rather than modeling time itself as a random variable, which leads to problems when combining events from multiple timelines, the key idea is to use an intensity function $\lambda$, which you can think of as the number of events per unit time. As an intensity function is not a density, it need not integrate to 1, rather the only technical constraint is that it has to be nonnegative. It also makes combining mutliple timelines straightforward (think for example about all stock trades for stocks in an index from the trades for the individual stocks) 

A few basic building blocks for temporal point processes are:
- The constant rate Poisson process, which is independent of history
- The inhomogenous Poisson process, with a time-dependent rate, but still independent of its own history
- The survival process, which has some value up to time t_s, and is 0 afterwards - note that this process depends on its own history
- The Hawkes process, a self-exciting process, useful to model clustered or bursty events (Exercise: can you come up with an example from finance?)

For all of the above, well-established techniques exist for sampling (mostly rejection sampling and potentialyly inverse sampling) and fitting (Maximum likelihood estimation) exist.

One can further generalise this by having mutually exciting processes, but at this point the classical schemes for sampling and inderence start to break down.

The second part of the tutorial 
