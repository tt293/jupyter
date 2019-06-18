# Notes on Deep Hedging

## Problem Setup

* Our setting is a discrete-time market where we can trade at time points <img src="/notes/tex/ecfb952e168fe71ef904631e3f09b26c.svg?invert_in_darkmode&sanitize=true" align=middle width=190.37981655pt height=22.465723500000017pt/>. 

* The prices of our hedging instruments are represented as a stochastic process <img src="/notes/tex/e46b2c414586d92f9ccea91501a7e01a.svg?invert_in_darkmode&sanitize=true" align=middle width=35.83918304999999pt height=24.65753399999998pt/> in <img src="/notes/tex/435f1061aa6f25938c3c3515c083d06c.svg?invert_in_darkmode&sanitize=true" align=middle width=18.71525699999999pt height=27.91243950000002pt/>.

* Selling a contingent claim with payoff <img src="/notes/tex/5b51bd2e6f329245d425b8002d7cf942.svg?invert_in_darkmode&sanitize=true" align=middle width=12.397274999999992pt height=22.465723500000017pt/> for price <img src="/notes/tex/2e1cdc8292853e76ffbb0b8d85d62c2a.svg?invert_in_darkmode&sanitize=true" align=middle width=14.823113249999992pt height=14.15524440000002pt/> and hedging using a predictable strategy <img src="/notes/tex/38f1e2a089e53d5c990a82f284948953.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928075099999989pt height=22.831056599999986pt/>, the P&L is:  

<p align="center"><img src="/notes/tex/096a646a5c6225d3a1b9fb129b9b1ebe.svg?invert_in_darkmode&sanitize=true" align=middle width=334.29599939999997pt height=44.89738935pt/></p> (1),

* Here <img src="/notes/tex/fc731b36fd97cbe31b8296fa953512fb.svg?invert_in_darkmode&sanitize=true" align=middle width=42.81794714999999pt height=24.65753399999998pt/> denote the cumulative transaction costs. We also use <img src="/notes/tex/5987f0961e0c1c6d9713c05613d81ef4.svg?invert_in_darkmode&sanitize=true" align=middle width=53.14658744999999pt height=24.65753399999998pt/> as a more concise notation for the hedging P&L.

* <img src="/notes/tex/99f2aca797dbfd7f0bafd965762349f9.svg?invert_in_darkmode&sanitize=true" align=middle width=113.5004013pt height=24.65753399999998pt/> represents a profit for us.


## Indifference pricing

### Risk-adjusted return measure

We choose a concave risk measure <img src="/notes/tex/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode&sanitize=true" align=middle width=13.08219659999999pt height=22.465723500000017pt/>, which makes <img src="/notes/tex/b58b11372a7fecc92a3b2d56211387e4.svg?invert_in_darkmode&sanitize=true" align=middle width=25.86762914999999pt height=22.465723500000017pt/> a conxex risk measure. We put several assumptions on our risk measure <img src="/notes/tex/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode&sanitize=true" align=middle width=13.08219659999999pt height=22.465723500000017pt/>:
* Monotonicity: <img src="/notes/tex/b83d9b040a6bad6d817eb30ba1a4e672.svg?invert_in_darkmode&sanitize=true" align=middle width=196.52914709999996pt height=24.65753399999998pt/>
* Normalization: <img src="/notes/tex/8fa02a329eb2305c70e9535e91912961.svg?invert_in_darkmode&sanitize=true" align=middle width=64.2236595pt height=24.65753399999998pt/>
* Cash Invariance: <img src="/notes/tex/2d427652ee9f35cb440dca046c8b361a.svg?invert_in_darkmode&sanitize=true" align=middle width=157.88017574999998pt height=24.65753399999998pt/> for any <img src="/notes/tex/38078c5daea8c0c56efcfd83cf0afe4d.svg?invert_in_darkmode&sanitize=true" align=middle width=39.077121599999984pt height=22.648391699999998pt/>. This is saying that cash, as a riskless instrument, linearly increases our risk-adjusted return.

 and denote the space of all admissible hedging strategies by <img src="/notes/tex/8209c0f8b3c5233ea2e20dae55588c43.svg?invert_in_darkmode&sanitize=true" align=middle width=14.041179899999989pt height=22.465723500000017pt/>. Then the indifference price is the solution to   

<p align="center"><img src="/notes/tex/1a2d09117b3cb567ecc6f8a70e297cb5.svg?invert_in_darkmode&sanitize=true" align=middle width=306.0003342pt height=23.9301051pt/></p> (2)
or, in other words: we do not care whether we sell the contingent claim or not. We denote the minimizing hedging strategy by <img src="/notes/tex/2f9d1973a833a7945d0810cf857c3bcb.svg?invert_in_darkmode&sanitize=true" align=middle width=14.66326619999999pt height=22.831056599999986pt/>.

In any realistic setup, it is not feasible to numerically compute <img src="/notes/tex/6265e5337d0c3db74f7b9eb6e3a1a026.svg?invert_in_darkmode&sanitize=true" align=middle width=33.45326819999999pt height=24.65753399999998pt/> and <img src="/notes/tex/2f9d1973a833a7945d0810cf857c3bcb.svg?invert_in_darkmode&sanitize=true" align=middle width=14.66326619999999pt height=22.831056599999986pt/>, but we hope that with deep learning we can find a good approximate solution.

We will consider only hedging strategies of the form  

<p align="center"><img src="/notes/tex/30969e02dbf04b7a134e3042f2e468b8.svg?invert_in_darkmode&sanitize=true" align=middle width=161.7414117pt height=20.35808775pt/></p> (3)

where <img src="/notes/tex/bc29af2d583d502a65b1bbd2bb404af4.svg?invert_in_darkmode&sanitize=true" align=middle width=25.47954749999999pt height=27.91243950000002pt/> is a neural network.

Using this, our indifference price <img src="/notes/tex/6265e5337d0c3db74f7b9eb6e3a1a026.svg?invert_in_darkmode&sanitize=true" align=middle width=33.45326819999999pt height=24.65753399999998pt/> is given by:  

<p align="center"><img src="/notes/tex/c5192b97e0d9716b96bd43cecb77f19d.svg?invert_in_darkmode&sanitize=true" align=middle width=220.1542299pt height=16.438356pt/></p> (4)
<p align="center"><img src="/notes/tex/eb9b023bf36936a676ddc481c8c04958.svg?invert_in_darkmode&sanitize=true" align=middle width=266.56826129999996pt height=23.9301051pt/></p> (5)

We approximate <img src="/notes/tex/4352960ca8d283359c12eaed0eae4540.svg?invert_in_darkmode&sanitize=true" align=middle width=37.65418799999999pt height=24.65753399999998pt/> by 

<p align="center"><img src="/notes/tex/68b81731d57e35ae6adc33a53272b60d.svg?invert_in_darkmode&sanitize=true" align=middle width=291.89498414999997pt height=24.71231565pt/></p> (6)

One example of such a risk measure is the <img src="/notes/tex/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>-CVaR measure 

<p align="center"><img src="/notes/tex/ed27ac7abbb6d59167cac65ddd7c84e7.svg?invert_in_darkmode&sanitize=true" align=middle width=239.01242475pt height=28.644343199999998pt/></p> (7)

