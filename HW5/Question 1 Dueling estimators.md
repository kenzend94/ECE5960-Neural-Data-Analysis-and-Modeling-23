## Question 1: Dueling estimators.

In this problem, we use simulation to compare three estimators of the mean of a Normal (Gaussian) distribution.

  - (a) First consider the average, which minimizes the sum of squared deviations, and is also the Maximum Likelihood estimator. Generate 10,000 samples, each of size 10, from the Normal(0,1) distribution (a 10x10000 matrix). Compute the average of each of the 10,000 samples. Plot a histogram of the resulting estimates (use 50 bins, and set the plot range to [-2.3,2.3]). What shape should the histogram have (explain why)? What is the (theoretical) variance of the average of 10 values drawn from a univariate Gaussian (derive this)? Is the empirical variance of your 10,000 estimates close to this?

  - (b) Now consider the median, which minimizes the sum of absolute deviations. Compute the median of each of the 10,000 samples, and again plot a histogram. What shape does this one have? Compare it to a normal distribution using the function normplot, which plots the quantiles of a sample of data versus the normal quantiles (known as a Q-Q plot: if data are normally distributed, the points shuld fall nearly on a straight line.) Does the distribution of estimated values deviate significantly from a Normal distribution? Specifically, compare the Q-Q plot for the median estimator to that for the mean from part (a).

  - (c) Finally, consider an estimator that computes the average of the minimum and maximum over the sample (as shown in class, this one minimizes the L∞−norm). Again, compute this estimate for each of your 10,000 samples, plot the histogram, and examine and comment on the Q-Q plot, just as in part (b).

  - (d) All three of these estimators are unbiased (because of the symmetry of the distribution), so we can use variance as the sole criterion for quality. Generate a new set of 10,000 samples, this time of dimension 256. Apply each estimator to sub-matrices of samples of size {8, 16, 32, 64, 128, 256}, and compute the variance of each estimator for each. Plot these (on a single log-log plot), along with a line showing the theoretically-computed variance of the average estimator. Does the variance of all three estimators converge at the same rate (1/N )? How much larger is the variance of the median estimator than the average estimator? How large a sample would you need for the average and median estimators to achieve the same variance as the average-extrema estimator (from part (c)) on samples of size 256?

### Part a:

First consider the average, which minimizes the sum of squared deviations, and is also the Maximum Likelihood estimator. Generate 10,000 samples, each of size 10, from the Normal(0,1) distribution (a 10x10000 matrix). Compute the average of each of the 10,000 samples. Plot a histogram of the resulting estimates (use 50 bins, and set the plot range to [-2.3,2.3]). What shape should the histogram have (explain why)? What is the (theoretical) variance of the average of 10 values drawn from a univariate Gaussian (derive this)? Is the empirical variance of your 10,000 estimates close to this?


    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_3_0.png)
    


    Theoretical variance:  0.1
    Empirical variance:  0.0983455237173575
    As you can see, the empirical variance is close to the theoretical variance.
    

### Part b:

Now consider the median, which minimizes the sum of absolute deviations. Compute the median of each of the 10,000 samples, and again plot a histogram. What shape does this one have? Compare it to a normal distribution using the function normplot, which plots the quantiles of a sample of data versus the normal quantiles (known as a Q-Q plot: if data are normally distributed, the points shuld fall nearly on a straight line.) Does the distribution of estimated values deviate significantly from a Normal distribution? Specifically, compare the Q-Q plot for the median estimator to that for the mean from part (a).


    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_5_0.png)
    



    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_5_1.png)
    


### Part c:

Finally, consider an estimator that computes the average of the minimum and maximum over the sample (as shown in class, this one minimizes the L∞−norm). Again, compute this estimate for each of your 10,000 samples, plot the histogram, and examine and comment on the Q-Q plot, just as in part (b).


    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_7_0.png)
    



    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_7_1.png)
    


### Part d:

All three of these estimators are unbiased (because of the symmetry of the distribution), so we can use variance as the sole criterion for quality. Generate a new set of 10,000 samples, this time of dimension 256. Apply each estimator to sub-matrices of samples of size {8, 16, 32, 64, 128, 256}, and compute the variance of each estimator for each. Plot these (on a single log-log plot), along with a line showing the theoretically-computed variance of the average estimator. Does the variance of all three estimators converge at the same rate (1/N )? How much larger is the variance of the median estimator than the average estimator? How large a sample would you need for the average and median estimators to achieve the same variance as the average-extrema estimator (from part (c)) on samples of size 256?


    
![png](Question%201%20Dueling%20estimators_files/Question%201%20Dueling%20estimators_9_0.png)
    


    Mean variance:  [0.12472000154010304, 0.0633627747212971, 0.03098832629633028, 0.01556328692871835, 0.007782577524438304, 0.003916802592995878]
    Median variance:  [0.17228866461461959, 0.09158283019894779, 0.04633518068316906, 0.023643355151655922, 0.01201241848253454, 0.0060982522814742035]
    Min-Max variance:  [0.20075451289356855, 0.15665257794732007, 0.1245305206878975, 0.10183536401847043, 0.08785513284613758, 0.07729820934295116]
    Theoretical mean variance:  [0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625]
    
