## Question 1: Fitting a psychometric function.

In  HW5-Q4, we simulated a subject performing a 2-alternative forced choice psychophysics experiment. We will now simulate the inverse (scientific) side of the problem, and use this probabilistic model as a means of fitting/analyzing a simulated data set.

  - (a) Write a function ```nll = nloglik(mu, sigma, I, T, C)``` that returns the negative log likelihood of parameters mu and sigma, for data set I, T, C (we’re negating it because we will be minimizing this function to solve for the optimal parameters).

  - (b) Generate a contour plot (function contour, using 50 lines) of the negative log likelihood of the data set from part (c) of the previous problem, for all pairs of mu from muall= [2:0.2:10] and a ```sigma``` from ```sigmaall``` = [0.5:0.2:6]. What is the approximate location of the best fitting pair of parameters from this plot?

  - (c) Use the matlab function ```fminsearch``` to get a more precise estimate of values mu,sigma that minimize the function ```nloglik(mu,sigma,...)```. Two comments: first,the syntax for calling nloglik within fminsearch is a bit odd: ```fminsearch(@(x) nloglik(x(1),x(2),I,T,C), <startpoint>)```.Here, the @ notation is used to create a temporary function, with argument x a vector containing the two variables being optimized (mean and stdev).  Second, you’ll need to specify a start point for the search – for this problem, [2,2] is a reasonable choice.

  - (d) A variant of ```fminsearch```, ```fminunc```, also returns the Hessian(the matrix of second derivatives) of the negative log likelihood at the optimal mu and sigma. (Note: ```fminunc``` is less robust than ```fminsearch```, and if the optimizer strays too far from the true values,there may be numerical problems due to overflow of the likelihood; in this case, try a different starting point.) The inverse of the Hessian provides an estimate of the covariance matrix of the parameter estimates. Use this to determine 95% confidence intervals on each parameter (Hint: a 95% confidence interval is the mean ±1.96 standard deviations of the parameter estimate. Compute the standard deviation of a marginal of the 2-D Gaussian that has covariance equal to the inverse Hessian.)  Do the true parameter values (4 and 1) fall within these confidence intervals?

  - (e) Produce a second set of confidence intervals for the parameters using a bootstrap method.For each of the 7 intensities, resample 100 trials (correct or incorrect) from the 100 trials of that intensity in the original data, with replacement.  Refit the model to the resampled data using ```fminsearch```.  Plot the histograms (function hist) of mu and sigma estimates obtained over 500 such resampled datasets, and define your confidence intervals as the 2 region between the 2.5th and 97.5th percentiles of these distributions. How well do these values agree with those from part (d)?


### Part a:

Write a function ```nll = nloglik(mu, sigma, I, T, C)``` that returns the negative log likelihood of parameters mu and sigma, for data set I, T, C (we’re negating it because we will be minimizing this function to solve for the optimal parameters).

### Part b:

Generate a contour plot (function contour, using 50 lines) of the negative log likelihood of the data set from part (c) of the previous problem, for all pairs of mu from muall= [2:0.2:10] and a ```sigma``` from ```sigmaall``` = [0.5:0.2:6]. What is the approximate location of the best fitting pair of parameters from this plot?

    I (Intensity): [1 2 3 4 5 6 7]
    T (Trials): [100. 100. 100. 100. 100. 100. 100.]
    C (Correct Responses): [50.0, 51.0, 57.0, 75.0, 92.0, 98.0, 99.0]
    


    
![png](Question%201%20Fitting%20a%20psychometric%20function_files/Question%201%20Fitting%20a%20psychometric%20function_5_1.png)
    


### Part c:

Use the matlab function ```fminsearch``` to get a more precise estimate of values mu,sigma that minimize the function ```nloglik(mu,sigma,...)```. Two comments: first,the syntax for calling nloglik within fminsearch is a bit odd: ```fminsearch(@(x) nloglik(x(1),x(2),I,T,C), <startpoint>)```.Here, the @ notation is used to create a temporary function, with argument x a vector containing the two variables being optimized (mean and stdev).  Second, you’ll need to specify a start point for the search – for this problem, [2,2] is a reasonable choice.

    Optimal mu: -1.5340244262792964
    Optimal sigma: 3.668422881117816
    

### Part d:

A variant of ```fminsearch```, ```fminunc```, also returns the Hessian(the matrix of second derivatives) of the negative log likelihood at the optimal mu and sigma. (Note: ```fminunc``` is less robust than ```fminsearch```, and if the optimizer strays too far from the true values,there may be numerical problems due to overflow of the likelihood; in this case, try a different starting point.) The inverse of the Hessian provides an estimate of the covariance matrix of the parameter estimates. Use this to determine 95% confidence intervals on each parameter (Hint: a 95% confidence interval is the mean ±1.96 standard deviations of the parameter estimate. Compute the standard deviation of a marginal of the 2-D Gaussian that has covariance equal to the inverse Hessian.)  Do the true parameter values (4 and 1) fall within these confidence intervals?

    Optimal mu: -1.5340244262792964
    Optimal sigma: 3.668422881117816
    95% CI for mu: (-28.071690046704397, 25.003641194145807)
    95% CI for sigma: (-8.647903353213712, 15.984749115449345)
    Does true mu fall within the 95% CI? True
    Does true sigma fall within the 95% CI? True
    

### Part e:

Produce a second set of confidence intervals for the parameters using a bootstrap method.For each of the 7 intensities, resample 100 trials (correct or incorrect) from the 100 trials of that intensity in the original data, with replacement.  Refit the model to the resampled data using fminsearch.  Plot the histograms (function hist) of mu and sigma estimates obtained over 500 such resampled datasets, and define your confidence intervals as the 2 region between the 2.5th and 97.5th percentiles of these distributions. How well do these values agree with those from part (d)?


    
![png](Question%201%20Fitting%20a%20psychometric%20function_files/Question%201%20Fitting%20a%20psychometric%20function_11_0.png)
    


    Bootstrap 95% CI for mu: [-5.54329862e+13  5.72730147e+00]
    Bootstrap 95% CI for sigma: [1.50259131e-01 2.55440908e+13]
    
