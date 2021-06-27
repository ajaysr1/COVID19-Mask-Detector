# Adam Optimizer
Adaptive Moment Estimation is an algorithm that optimizes the gradient descent. It is a combination of 'Gradient Descent with Momentum' algorithm and the 'RMSP' algorithm.
It is well suited for problems that are large in terms of data and/or parameters.

To understand the working of Adam, we need to first understand the above-mentioned algorithms.

## Gradient Descent with Momentum
To converge at the minima at a faster rate, this algorithm uses 'exponentially weighted average' of gradients to accelerate the gradient descent algorithm.

W<sub>t+1</sub> = W<sub>t</sub> - αm<sub>t</sub>
