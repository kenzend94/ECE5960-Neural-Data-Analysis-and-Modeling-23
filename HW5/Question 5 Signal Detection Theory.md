## Question 5: Signal Detection Theory.

Consider an experiment where a moving-dot visual stimulus is presented to a subject. The difficulty of detecting the motion is varied by changing the coherence of the moving dots  which is the fraction of dots moving to the right (at zero coherence, the dots move randomly, and at 100% coherence, all of the dots move to the right). Suppose we want to decide whether the stimulus is random or is moving to the right, based on the response of a single neuron that fires at a random rate, whose mean is 5 spikes/s in response to a 0% coherence noisy stimulus and 8 spikes/s for 10% coherence. Suppose also that the distribution of firing rates is Gaussian with a standard deviation of 1 spikes/s for both stimuli.

  - (a) For the “no coherence”’ stimulus, generate 1000 trials of the firing rate of the neuron in response to these stimuli (i.e., draw 1000 random samples from a Gaussian with μ = 5 and σ = 1). Since we cannot have negative firing rates, set all rates that are below zero to zero. Now do the same thing for the 10% coherence stimulus. On the same figure, plot the histograms of the firing rates for each stimulus type.

  - (b) The success of the decoder (assuming this model of Gaussian noise) is determined by two things, the separation of the mean firing rates and the standard deviation of the neuron. From class, we know that this is captured in the measure known as d′. Calculate d′ for this task and pair of stimuli (ignoring the fact that you are clipping firing rates at zero).

  - (c) Explain why the maximum likelihood decoder for this problem involves comparing the measurement to a threshold. For various thresholds t, calculate the hit and false-alarm rates using your sample data from (a), and plot these against each other (this is an ROC curve, defined in class). What threshold would you pick based on this curve to maximize the percentage-correct of the decoder, assuming that 0% and 10% coherence stimuli occur equally often. Plot this threshold as a point on the ROC curve and as a vertical line on your histogram from part (a). Next, suppose that 10% coherence stimuli occur 75% of the time. Determine and plot the threshold that maximizes percentage correct for this new prior.

  - (d) Consider now a neuron with a more ”noisy” response so that the mean firing rates are the same but the standard deviation is 2 spikes/s instead of 1 spike/s. What is the new value of d′. Recompute and plot the optimal (maximum accuracy) thresholds for this noisy neuron for both the 50-50 and 75-25 priors. How do they differ from those in the previous part?

### Part a:

For the “no coherence”’ stimulus, generate 1000 trials of the firing rate of the neuron in response to these stimuli (i.e., draw 1000 random samples from a Gaussian with μ = 5 and σ = 1). Since we cannot have negative firing rates, set all rates that are below zero to zero. Now do the same thing for the 10% coherence stimulus. On the same figure, plot the histograms of the firing rates for each stimulus type.



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_3_0.png)
    


### Part b:

The success of the decoder (assuming this model of Gaussian noise) is determined by two things, the separation of the mean firing rates and the standard deviation of the neuron. From class, we know that this is captured in the measure known as d′. Calculate d′ for this task and pair of stimuli (ignoring the fact that you are clipping firing rates at zero).


The d' value is calculated as the absolute difference between the mean firing rates divided by the standard deviation.

$$
d' = \frac{|\mu_1 - \mu_2|}{\sigma}
$$

    d' value: 3.0
    

### Part c:

Explain why the maximum likelihood decoder for this problem involves comparing the measurement to a threshold. For various thresholds t, calculate the hit and false-alarm rates using your sample data from (a), and plot these against each other (this is an ROC curve, defined in class). What threshold would you pick based on this curve to maximize the percentage-correct of the decoder, assuming that 0% and 10% coherence stimuli occur equally often. Plot this threshold as a point on the ROC curve and as a vertical line on your histogram from part (a). Next, suppose that 10% coherence stimuli occur 75% of the time. Determine and plot the threshold that maximizes percentage correct for this new prior.



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_8_0.png)
    


    Optimal Threshold: 6.515151515151516
    


    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_10_0.png)
    



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_10_1.png)
    


    Optimal Threshold with New Prior: 6.212121212121212
    


    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_12_0.png)
    



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_12_1.png)
    


### Part d:

Consider now a neuron with a more ”noisy” response so that the mean firing rates are the same but the standard deviation is 2 spikes/s instead of 1 spike/s. What is the new value of d′. Recompute and plot the optimal (maximum accuracy) thresholds for this noisy neuron for both the 50-50 and 75-25 priors. How do they differ from those in the previous part?



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_14_0.png)
    



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_14_1.png)
    


    d' value for noisy neuron: 1.5
    

    Optimal Threshold for Noisy Neuron: 6.515151515151516
    


    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_16_0.png)
    



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_16_1.png)
    


    Optimal Threshold with New Prior for Noisy Neuron: 4.696969696969697
    


    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_18_0.png)
    



    
![png](Question%205%20Signal%20Detection%20Theory_files/Question%205%20Signal%20Detection%20Theory_18_1.png)
    

