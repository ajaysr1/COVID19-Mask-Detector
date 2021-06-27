# Adam Optimizer
Adaptive Moment Estimation is an algorithm that optimizes the gradient descent. It is a combination of 'Gradient Descent with Momentum' algorithm and the 'RMSP' algorithm.
It is well suited for problems that are large in terms of data and/or parameters.

To understand the working of Adam, we need to first understand the above-mentioned algorithms.

## Gradient Descent with Momentum
To converge at the minima at a faster rate, this algorithm uses 'exponentially weighted average' of gradients to accelerate the gradient descent algorithm.

<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a689bde5453a6f62ce674379f21713ef_l3.svg" width="25%"></img></br>
where, <br/>
<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-11485c48aad57c3897036904bff90924_l3.svg" width="30%"></img></br>

## Root Mean Square Propagation (RMSP)
This algorithm uses 'exponential moving average'. It also adapts the learning rate based on the

<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c1f05c2b4b465f8fec637fc731d8777e_l3.svg" width="30%"></img></br>
<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a2ad3f644ee1350b15ae1675fc757338_l3.svg" width="30%"></img></br>
<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-30ada136b73bc4f46bdbb2cec115c84f_l3.svg" width="30%"></img></br>
<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-de49f2b3fa2b380dc7a56e824805c49a_l3.svg" width="30%"></img></br>
<img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-627062af6c0d34dae31b75b634c2e2cb_l3.svg" width="30%"></img></br>


