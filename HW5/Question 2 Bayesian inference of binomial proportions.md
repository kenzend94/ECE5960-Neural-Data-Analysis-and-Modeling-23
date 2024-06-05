## Question 2: Bayesian inference of binomial proportions.

Poldrack (2006) published an influential attack on the practice of ”reverse inference” in fMRI studies, i.e. inferring that a cognitive process was engaged on the basis of activation in some area. For instance, if Broca’s area was found to be activated using standard fMRI statistical-contrast techniques, researchers might infer that the subjects were using language. In a search of the literature, Poldrack found that Broca’s area was reported activated in 103 out of 869 fMRI contrasts involving engagement of language, but this area was also active in 199 out of 2353 contrasts not involving language.

  - (a) Assume that the conditional probability of activation given language, as well as that of activation given no language, each follow a Bernoulli distribution (i.e., like coin-flipping), with parameters xl and xnl. Compute the likelihoods of these parameters, given Poldrack’s observed frequencies of activation. Compute these functions at the values x=[0:.001:1] and plot them as a bar chart.

  - (b) Find the value of x that maximizes each discretized likelihood function. Compare these to the exact maximum likelihood estimates given by the formula for the ML estimator of a Bernoulli probability.

  - (c) Using the likelihood functions computed for discrete x, compute and plot the discrete posterior distributions P (x | data) and the associated cumulative distributions P (X ≤ x | data) for both processes. For this, assume a uniform prior P (x) ∝ 1 and note that it will be necessary to compute (rather than ignore) the normalizing constant for Bayes’ rule. Use the cumulative distributions to compute (discrete approximations to) upper and lower 95% confidence bounds on each proportion.

  - (d) Are these frequencies different from one another? Consider the joint posterior distribution over xl and xnl, the Bernoulli probability parameters for the language and non-language contrasts. Given that these two frequencies are independent, the (discrete) joint distribution is given by the outer product of the two marginals. Plot it (with imagesc). Compute (by summing the appropriate entries in the joint distribution) the posterior probabilities that xl > xnl and, conversely, that xl ≤ xnl.

  - (e) Is this difference sufficient to support reverse inference? Compute the probability P (language | activation). This is the probability that observing activation in Broca’s area implies engagement of language processes. To do this use the estimates from part (b) as the relevant conditional probabilities, and assuming the prior that a contrast engages language, P (language) = 0.5. Poldrack’s critique said that we cannot simply conclude that activation in a given area indicates that a cognitive process was engaged without computing the posterior probability. Is this critique correct? To answer this, compare the Bayes factor (probability of language vs. not language) after taking Poldrack’s data into account, compared to before having done so.


### Part a:

Assume that the conditional probability of activation given language, as well as that of activation given no language, each follow a Bernoulli distribution (i.e., like coin-flipping), with parameters xl and xnl. Compute the likelihoods of these parameters, given Poldrack’s observed frequencies of activation. Compute these functions at the values x=[0:.001:1] and plot them as a bar chart.



    
![png](Question%202%20Bayesian%20inference%20of%20binomial%20proportions_files/Question%202%20Bayesian%20inference%20of%20binomial%20proportions_4_0.png)
    


### Part a:

Find the value of x that maximizes each discretized likelihood function. Compare these to the exact maximum likelihood estimates given by the formula for the ML estimator of a Bernoulli probability.

    Language Contrasts:
    Max x for likelihood function via argmax: x = 0.11900100000000001, likelihood: -3.1749765587113927
    Theoretical max x (x_max = y/n): x = 0.11852704257767549
    
    Non-Language Contrasts:
    Max x for likelihood function via argmax: x = 0.08500100000000001, likelihood: -3.524607414652934
    Theoretical max x (x_max = y/n): x = 0.08457288567785805
    

### Part c:

Using the likelihood functions computed for discrete x, compute and plot the discrete posterior distributions P (x | data) and the associated cumulative distributions P (X ≤ x | data) for both processes. For this, assume a uniform prior P (x) ∝ 1 and note that it will be necessary to compute (rather than ignore) the normalizing constant for Bayes’ rule. Use the cumulative distributions to compute (discrete approximations to) upper and lower 95% confidence bounds on each proportion.


    
![png](Question%202%20Bayesian%20inference%20of%20binomial%20proportions_files/Question%202%20Bayesian%20inference%20of%20binomial%20proportions_8_0.png)
    



    
![png](Question%202%20Bayesian%20inference%20of%20binomial%20proportions_files/Question%202%20Bayesian%20inference%20of%20binomial%20proportions_8_1.png)
    


### Part d:

Are these frequencies different from one another? Consider the joint posterior distribution over xl and xnl, the Bernoulli probability parameters for the language and non-language contrasts. Given that these two frequencies are independent, the (discrete) joint distribution is given by the outer product of the two marginals. Plot it (with imagesc). Compute (by summing the appropriate entries in the joint distribution) the posterior probabilities that xl > xnl and, conversely, that xl ≤ xnl.


    
![png](Question%202%20Bayesian%20inference%20of%20binomial%20proportions_files/Question%202%20Bayesian%20inference%20of%20binomial%20proportions_10_0.png)
    


    Posterior probability that xl > xnl: 0.0016
    Posterior probability that xl ≤ xnl: 0.9984
    As we can see, the posterior probability that xl > xnl is greater than the posterior probability that xl ≤ xnl.
    Therefore, the frequencies are different from one another.
    

### Part e:

Is this difference sufficient to support reverse inference? Compute the probability P (language | activation). This is the probability that observing activation in Broca’s area implies engagement of language processes. To do this use the estimates from part (b) as the relevant conditional probabilities, and assuming the prior that a contrast engages language, P (language) = 0.5. Poldrack’s critique said that we cannot simply conclude that activation in a given area indicates that a cognitive process was engaged without computing the posterior probability. Is this critique correct? To answer this, compare the Bayes factor (probability of language vs. not language) after taking Poldrack’s data into account, compared to before having done so.

    P(language | activation): 0.5836
    Bayes factor (posterior odds / prior odds): 1.4015
    
