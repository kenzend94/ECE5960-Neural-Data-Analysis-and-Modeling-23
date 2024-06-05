## Question 3: Psychopathy.

You are interested in causes and treatment options for Psychopathy. You obtained a dataset, contained in the file psychopathy.mat obtained from a prison for violent offenders in upstate New York (not everyone in the prison is a psychopath, but they are more prevalent than in the general population). Each row represents data from one prisoner. All study participants underwent a structural scan with a mobile, truck-mounted MRI. The first data column contains the estimated cortical volume of paralimbic areas, relative to the population median, in $\text{cm}^3$. The second column contains the Hare Psychopathy Checklist (PCL-R) scores, which range from 0 to 40 (the higher the score, the more psychopathic traits someone exhibits). These scores are not distributed normally in the general population (median = 4) and definitely not normal in this subpopulation (median = 20). The third column indicates whether they already participated in an experimental treatment program known as ˆadecompression therapyˆa (0 = did not yet participate, 1 = did already participate). To avoid self-selection effects, everyone in this dataset agreed to the therapy, but prisoners were randomly assigned to an earlier and a later treatment group, so that the untreated prisoners could serve as a control group.

  - (a) You want to model PCL-R scores as a function of relative volume of paralimbic areas. Use polynomial regression to find a model that best explains the data using cross-validation. What degree does it have? (Note, you can use your code from HW2.)

  - (b) Use bootstrapping methods to estimate the 95% confidence interval of the average paralimbic volume of the decompression treatment group vs. the control group. If the random assignment worked, the confidence intervals should overlap. Do they? Also, do these data suggest that there is a statistically reliable difference to the general population in terms of paralimbic volume?

  - (c) Do a suitable t-test to compare the mean PCL-R score of prisoners who did and did not undergo decompression therapy. What is the p-value? Assuming an alpha-level of 0.05, is this difference significant? Can you reject the null hypothesis that decompression therapy is ineffective in terms of decreasing PCL-R scores? 

  - (d) Do a permutation test to assess whether decompression therapy has an effect. Designate an appropriate test statistic and calculate its exact p value.


### Part a:
You want to model PCL-R scores as a function of relative volume of paralimbic areas. Use polynomial regression to find a model that best explains the data using cross-validation. What degree does it have? (Note, you can use your code from HW2.)


    
![png](Question%203%20Psychopathy_files/Question%203%20Psychopathy_4_0.png)
    



    
![png](Question%203%20Psychopathy_files/Question%203%20Psychopathy_4_1.png)
    


    Degree of polynomial with lowest cross-validation error: 3
    

### Part b:

Use bootstrapping methods to estimate the 95% confidence interval of the average paralimbic volume of the decompression treatment group vs. the control group. If the random assignment worked, the confidence intervals should overlap. Do they? Also, do these data suggest that there is a statistically reliable difference to the general population in terms of paralimbic volume?


    
![png](Question%203%20Psychopathy_files/Question%203%20Psychopathy_6_0.png)
    


    Interpretation of the results:
    The confidence intervals for the two groups overlap, so there is no statistically significant difference between the groups.
    However, the confidence intervals for both groups are significantly lower than the societal norm of 100 cm^3.
    Overlap of confidence intervals can be visually inspected from the plot.
    

### Part c:

Do a suitable t-test to compare the mean PCL-R score of prisoners who did and did not undergo decompression therapy. What is the p-value? Assuming an alpha-level of 0.05, is this difference significant? Can you reject the null hypothesis that decompression therapy is ineffective in terms of decreasing PCL-R scores? 

    T-statistic: -1.7283246500731968
    P-value: 0.08846869073864871
    Fail to reject the null hypothesis. There is not enough evidence of a statistically significant difference between the groups.
    

### Part d:

Do a permutation test to assess whether decompression therapy has an effect. Designate an appropriate test statistic and calculate its exact p value.

    Observed Difference in Means: -3.2285714285714278
    P-value from Permutation Test: 0.09
    Result is not statistically significant - fail to reject the null hypothesis.
    
