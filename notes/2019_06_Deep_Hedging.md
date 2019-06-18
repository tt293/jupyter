# Notes on Deep Hedging

## Problem Setup

* Our setting is a discrete-time market where we can trade at time points $t_0 = 0 < t_1 < \ldots < t_n = T$. 

* The prices of our hedging instruments are represented as a stochastic process $(S_{t_k})$ in $\mathbb{R}^d$.

* Selling a contingent claim with payoff $Z$ for price $p_0$ and hedging using a predictable strategy $\delta$, the P&L is:  

$$ P_t = -Z + p_0 + \sum_{i=1}^n \delta_{t_k}\cdot(S_{t_k} - S_{t_{k-1}}) - C_T(\delta)$$ (1),

* Here $C_T(\delta)$ denote the cumulative transaction costs. We also use $(\delta \cdot S)_T$ as a more concise notation for the hedging P&L.

* $P_T(Z, p_0, \delta) \geq 0$ represents a profit for us.


## Indifference pricing

### Risk-adjusted return measure

We choose a concave risk measure $E$, which makes $-E$ a conxex risk measure. We put several assumptions on our risk measure $E$:
* Monotonicity: $X \geq Y \implies E(X) \geq E(Y)$
* Normalization: $E(0) = 0$
* Cash Invariance: $E(X+c) = E(X) + c$ for any $c \in \mathbb{R}$. This is saying that cash, as a riskless instrument, linearly increases our risk-adjusted return.

 and denote the space of all admissible hedging strategies by $\mathcal{H}$. Then the indifference price is the solution to   

$$ \inf_{\delta \in \mathcal{H}} E(P_T(Z, p(Z), \delta)) = \inf_{\delta \in \mathcal{H}} E(P_T(0, 0, \delta)) $$ (2)
or, in other words: we do not care whether we sell the contingent claim or not. We denote the minimizing hedging strategy by $\delta^*$.

In any realistic setup, it is not feasible to numerically compute $p(Z)$ and $\delta^*$, but we hope that with deep learning we can find a good approximate solution.

We will consider only hedging strategies of the form  

$$ \delta_{t_k} = F^{\theta_k}(S_{t_{k-1}}, \delta_{t_{k-1}}) $$ (3)

where $F^{\theta_k}$ is a neural network.

Using this, our indifference price $p(Z)$ is given by:  

$$ p(Z) = \pi(-Z) - \pi(0),\quad \mathrm{where} $$ (4)
$$ \pi(X) = \inf_{\delta \in \mathcal{H}} E(X + (\delta \cdot S)_T - C_T(\delta)) $$ (5)

We approximate $\pi(X)$ by 

$$ \pi_M(X) = \inf_{\theta \in \Theta_M} E(X + (\delta \cdot S)_T - C_T(\delta))  $$ (6)

One example of such a risk measure is the $\alpha$-CVaR measure 

$$ E(X) = \sup_{w \in \mathbb{R}} \{ w - \lambda \mathbb{E}[(w-X)^+] \} $$ (7)

