# Adam Optimizer
Adaptive Moment Estimation is an algorithm that optimizes the gradient descent. It is a combination of 'Gradient Descent with Momentum' algorithm and the 'RMSP' algorithm.
It is well suited for problems that are large in terms of data and/or parameters.

To understand the working of Adam, we need to first understand the above mentioned algorithms.

## Gradient Descent with Momentum
To converge at the minima at a faster rate, this algorithm uses 'exponentially weighted average' of gradients to accelerate the gradient descent algorithm.
<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a689bde5453a6f62ce674379f21713ef_l3.svg" width="20%">
</p> 
where, <br/>
<p align="center">  
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-11485c48aad57c3897036904bff90924_l3.svg" width="30%"></img></br>
</p>

m<sub>t</sub> = aggregate of gradients at time t(current) (initially, m<sub>t</sub> = 0) <br/>
m<sub>t-1</sub> = aggregate of gradients at time t-1(previous) <br/>
W<sub>t</sub> = weights at time t <br/>
W<sub>t+1</sub> = weights at time t+1 <br/>
α<sub>t</sub> = learning rate at time t <br/>
∂<sub>L</sub> = derivative of Loss Function <br/>
∂W<sub>t</sub> = derivative of weights at time t <br/>
β = Moving average parameter (const, 0.9) <br/>

## Root Mean Square Propagation (RMSP)
This algorithm is similar to 'Gradient Descent with Momentum' algorithm. The major difference is how the gradients are calculated. RMSP uses 'exponential moving average' instead of 'exponentially weighted average'. The learning rates gets adapted based on the average of recent magnitudes of the gradients for the weight.
<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c1f05c2b4b465f8fec637fc731d8777e_l3.svg" width="35%"></img></br>
</p>
where, <br/>
<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a2ad3f644ee1350b15ae1675fc757338_l3.svg" width="35%"></img></br>
</p>

W<sub>t</sub> = weights at time t <br/>
W<sub>t+1</sub> = weights at time t+1 <br/>
α<sub>t</sub> = learning rate at time t <br/>
∂<sub>L</sub> = derivative of Loss Function <br/>
∂W<sub>t</sub> = derivative of weights at time t <br/>
v<sub>t</sub> = sum of square of past gradients (initially, v<sub>t</sub> = 0) <br/>
β = Moving average parameter (const, 0.9) <br/>
ϵ = A small positive constant (10-8) <br/>

## Working of Adam Optimizer
Adam Optimizer uses the positive aspects of these two algorithms and builds upon it giving a more optimized gradient descent. <br/>
We rate of gradient descent is controlled in such a way that the step-size reduces as we reach the global minima and increases as we are far away from it. This is donw so that we do not converge at a local minima.

<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-30ada136b73bc4f46bdbb2cec115c84f_l3.svg" width="70%"></img></br>
</p>

ϵ = a small +ve constant to avoid 'division by 0' error when (v<sub>t</sub> -> 0). (10-8) <br/>
β<sub>1</sub> & β<sub>2</sub> = decay rates of average of gradients in the above two methods. (β<sub>1</sub> = 0.9 & β<sub>2</sub> = 0.999) <br/>
α — Step size parameter / learning rate (0.001) <br/>

Now, m<sub>t</sub> and v<sub>t</sub> both have been initialized as '0'. So, they gain a tendency to be baised towards '0'. To prevent this, Adam used 'bias-corrected' m<sub>t</sub> and v<sub>t</sub>.

<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-de49f2b3fa2b380dc7a56e824805c49a_l3.svg" width="25%"></img></br>
</p>

So the general equation that Adam uses is -
<p align="center">
  <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-627062af6c0d34dae31b75b634c2e2cb_l3.svg" width="30%"></img></br>
</p>
