## Question 4: Simulating a 2AFC experiment.

Consider a two-alternative forced choice (2AFC) psychophysical experiment in which a subject sees two stimulus arrays of some intensity on a trial and must say which one contains the target. (One and only one contains the target.) Her probability of being correct on a trial is:

$$
p_c(I) = \frac{1}{2} + \frac{1}{2}\Phi(I; \mu, \sigma)
$$

where Φ(I; μ, σ) is the cumulative distribution function of the Gaussian (normcdf in matlab) with mean μ and standard deviation σ evaluated at I. The function $p_c(I)$ is known as the psychometric function. (Minor note, somewhat subtle: This setup only makes sense if I is on a logarithmic scale, e.g., I = k log C, where C is stimulus contrast.)

  - (a) Plot two psychometric functions, for {μ, σ} equal to {5, 2} and {4, 3}. (Use I = [1 : 10]). Describe the difference between these. If you increase μ, how does the curve change? If you increase σ, how does the curve change? (If you are not sure, make more plots with different parameter values.) What is the range of pc(I)? Explain why this range is appropriate.

  - (b) Write a function C=simpsych(mu,sigma,I,T) which takes two vectors (I,T) of the same length, containing a list of intensities and the number of trials for each intensity, respectively, simulates draws from pc(I), and returns a vector, C, of the same length as I and T , which contains the number of trials correct out of T , at each intensity I.

  - (c) Illustrate the use of simpsych with T=ones(1,7)*100 and I=1:7 for μ = 4 and σ = 1. Plot C ./ T vs I (as points) and plot the psychometric function pc(I) (as a curve) on the same graph.

  - (d) Do the same with T=ones(1,7)*10 and plot the results (including the psychometric function). What is the difference between this and the plot of the previous question?



### Part a:

Plot two psychometric functions, for {μ, σ} equal to {5, 2} and {4, 3}. (Use I = [1 : 10]). Describe the difference between these. If you increase μ, how does the curve change? If you increase σ, how does the curve change? (If you are not sure, make more plots with different parameter values.) What is the range of pc(I)? Explain why this range is
appropriate.


    
![png](Question%204%20Simulating%20a%202AFC%20experiment_files/Question%204%20Simulating%20a%202AFC%20experiment_4_0.png)
    


    Interpretation of changes in µ and σ on the psychometric function
    The range of pc(I) is between 0.5 (chance level) and 1 (perfect accuracy).
    Increasing µ shifts the curve rightward, and increasing σ flattens the curve.
    

### Part b:

Write a function C=simpsych(mu,sigma,I,T) which takes two vectors (I,T) of the same length, containing a list of intensities and the number of trials for each intensity, respectively, simulates draws from pc(I), and returns a vector, C, of the same length as I and T , which contains the number of trials correct out of T , at each intensity I.

### Part c:

Illustrate the use of simpsych with T=ones(1,7)*100 and I=1:7 for μ = 4 and σ = 1. Plot C ./ T vs I (as points) and plot the psychometric function pc(I) (as a curve) on the same graph.


    
![png](Question%204%20Simulating%20a%202AFC%20experiment_files/Question%204%20Simulating%20a%202AFC%20experiment_8_0.png)
    


### Part d:

Do the same with T=ones(1,7)*10 and plot the results (including the psychometric function). What is the difference between this and the plot of the previous question?


    
![png](Question%204%20Simulating%20a%202AFC%20experiment_files/Question%204%20Simulating%20a%202AFC%20experiment_10_0.png)
    


    The difference between the two plots is that the plot with fewer trials is more noisy.
    


