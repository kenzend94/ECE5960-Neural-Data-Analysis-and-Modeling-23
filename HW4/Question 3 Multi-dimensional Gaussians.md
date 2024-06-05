## Question 3: Multi-dimensional Gaussians.

  - (a) Write a function ```samples = ndRandn(mean, cov, num)``` that generates a set of samples drawn from an N-dimensional Gaussian distribution with the specified ```mean``` (an N-vector) and ```cov```ariance (an NxN matrix). The parameter ```num``` should be optional (defaulting to 1) and should specify the number of samples to return. The returned value should be a matrix with ```num``` rows each containing a sample of N elements. (Hint: use the MATLAB function ```randn``` to generate samples from an N-dimensional Gaussian with zero mean and identity covariance matrix, and then transform these to achieve the desired mean/cov. Recall that the covariance of Y = MX is $E(YY^{T}) = MC_{X}M^{T} \ $ where $C_{X}\ $ is the covariance of X). Please use mean $\mu\ $ = [4; 5] with $C_{X}\ $ = [9;-5;-5; 6] to sample and scatterplot 1,000 points to verify your function work as intended.

  - (b) Now consider the marginal distribution of a generalized 2-D Gaussian with mean $\mu\ $ and covariance $\sum\ $ in which samples are projected onto a unit vector $\hat{u}\ $  to obtain a 1-D distribution. Write a mathematical expression for the mean, $\hat{\mu}\ $, and variance, $\hat{\sigma}^2 $, of this marginal distribution as a function of $\hat{u}\ $ and check it for a set of 48 unit vectors spaced evenly around the unit circle. For each of these, compare the mean and variance predicted from your mathematical expression to the sample mean and variance estimated by projecting your 1,000 samples from part (a) onto $\hat{u}\ $. Stem plot the mathematically computed mean and the sample mean (on the same plot), and also plot the mathematical variance and the sample variance.

  - (c) Now scatterplot 1,000 new samples of a 2-dimensional Gaussian using $\mu\ $ and $C_{X}\ $ in part (a). Measure the sample mean and covariance of your data points, comparing to the values that you requested when calling the function. Plot an ellipse on top of the scatterplot by generating unit vectors equi-spaced around the circle, and transforming them with a matrix as in part (a) to have the same mean and covariance as the data. Try this on three additional random data sets with different means and covariance matrices. Does this ellipse capture the shape of the data?

  - (d) How would you, mathematically, compute the direction (unit vector) that maximizes the variance of the marginal distribution? Compute this direction and verify that it is consistent with your plot.



### Part a:
Write a function ```samples = ndRandn(mean, cov, num)``` that generates a set of samples drawn from an N-dimensional Gaussian distribution with the specified ```mean``` (an N-vector) and ```cov```ariance (an NxN matrix). The parameter ```num``` should be optional (defaulting to 1) and should specify the number of samples to return. The returned value should be a matrix with ```num``` rows each containing a sample of N elements. (Hint: use the MATLAB function ```randn``` to generate samples from an N-dimensional Gaussian with zero mean and identity covariance matrix, and then transform these to achieve the desired mean/cov. Recall that the covariance of Y = MX is $E(YY^{T}) = MC_{X}M^{T} \ $ where $C_{X}\ $ is the covariance of X). Please use mean $\mu\ $ = [4; 5] with $C_{X}\ $ = [9;-5;-5; 6] to sample and scatterplot 1,000 points to verify your function work as intended.


    
![png](Question%203%20Multi-dimensional%20Gaussians_files/Question%203%20Multi-dimensional%20Gaussians_4_0.png)
    


### Part b:

Now consider the marginal distribution of a generalized 2-D Gaussian with mean $\mu\ $ and covariance $\sum\ $ in which samples are projected onto a unit vector $\hat{u}\ $  to obtain a 1-D distribution. Write a mathematical expression for the mean, $\hat{\mu}\ $, and variance, $\hat{\sigma}^2 $, of this marginal distribution as a function of $\hat{u}\ $ and check it for a set of 48 unit vectors spaced evenly around the unit circle. For each of these, compare the mean and variance predicted from your mathematical expression to the sample mean and variance estimated by projecting your 1,000 samples from part (a) onto $\hat{u}\ $. Stem plot the mathematically computed mean and the sample mean (on the same plot), and also plot the mathematical variance and the sample variance.


    
![png](Question%203%20Multi-dimensional%20Gaussians_files/Question%203%20Multi-dimensional%20Gaussians_6_0.png)
    


### Part c:
Now scatterplot 1,000 new samples of a 2-dimensional Gaussian using $\mu\ $ and $C_{X}\ $ in part (a). Measure the sample mean and covariance of your data points, comparing to the values that you requested when calling the function. Plot an ellipse on top of the scatterplot by generating unit vectors equi-spaced around the circle, and transforming them with a matrix as in part (a) to have the same mean and covariance as the data. Try this on three additional random data sets with different means and covariance matrices. Does this ellipse capture the shape of the data?

    Means of samples measured: [4.02657677 4.97815823] vs requested means: [[ 9 -5]
     [-5  6]].
    Covariance of samples measured:
    [[11.23058156 -7.09960328]
     [-7.09960328  9.22285971]]
     vs requested covariance: 
    [[ 9 -5]
     [-5  6]].
    
    Requested parameters are similar to the measured parameters.
    


    
![png](Question%203%20Multi-dimensional%20Gaussians_files/Question%203%20Multi-dimensional%20Gaussians_8_1.png)
    


Q: Does this ellipse capture the shape of the data?
A: The ellipse shows how your data spreads out. It's centered where your data averages out and stretches more in the directions where your data varies most. This gives a quick visual idea of the data's spread and variation.

### Part d:

How would you, mathematically, compute the direction (unit vector) that maximizes the variance of the marginal distribution? Compute this direction and verify that it is consistent with your plot.


    
![png](Question%203%20Multi-dimensional%20Gaussians_files/Question%203%20Multi-dimensional%20Gaussians_11_0.png)
    

