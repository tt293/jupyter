ICML, Day 1: Tutorials

The first day of ICML consisted of a full day of tutorial sessions, for a full list see [ICML Schedule](https://icml.cc/Conferences/2018/Schedule?type=Tutorial). 
For the morning session, I decided to attend [Learning With Temporal Point Processes](http://learning.mpi-sws.org/tpp-icml18/):

Temporal point processes start from the observation that most time series are noisy observations of complex processes, observed asynchronously and at irregularly sampled intervals. In practice, a commonly used workaround to this is aggragating observations over an interval, but this leads to questions like how long the interval should be, how to handle intervals with 0 observations and so on.

Some applications outside finance are information propagation in socail networks or modelling infectious disease propagations.

Definition: A *temporal point process* is a random process whose realization consists of discrete events localized in time.

Rather than modeling time itself as a random variable, which leads to problems when combining events from multiple timelines, the key idea is to use an intensity function $\lambda$
