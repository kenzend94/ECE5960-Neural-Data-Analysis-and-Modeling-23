## Question 5: Sampling and aliasing

Load the file ```myMeasurements.mat``` into matlab. It contains a vector, ```sig```, containing voltage values measured from an EEG electrode, sampled at 100Hz. Plot ```sig``` as a function of vector ```time``` (time, in seconds), using the flag ’ko-’ in matlab’s plot command so you can see the samples.

  - (a) This signal is only a small portion of the full data, and you don’t want to store all those values. Create a subsampled version of the signal, which contains every fourth value. Plot this, against the corresponding entries of the ```time``` vector, on top of the original data (use matlab’s ```hold``` function, and plot with flag ’r*-’). How does this reduced version of the data look, compared to the original? Does it provide a good summary of the original measurements? Is the subsampling operation linear? Shift-invariant? Explain.

  - (b) Examine your EEG result in the frequency domain. First plot the magnitude (amplitude) of the Fourier transform of the original signal, over the range [􀀀N=2; (N=2) 􀀀 1] (use ```fftshift```). By convention, the ”Delta” band corresponds to frequencies less than 4Hz, ”Theta” band is 4-7Hz, ”Alpha” band 8-15Hz, and ”Beta” is 16-31Hz. For these data, which band shows the strongest signal?

  - (c) Plot the Fourier magnitude for signals downsampled by factors of 2, 3, and 4, after upsampling them back to full size (i.e., make a full-size signal filled with zeros, and set every kth sample equal to one of the subsampled values, for subsampling by factor k). What is the relationship between these plots and the original frequency plot. What has happened to the frequency components of the original signal? Does the strongest signal band change?






### Plot signal


    
![png](Question%205%20Sampling%20and%20aliasing_files/Question%205%20Sampling%20and%20aliasing_5_0.png)
    


### Part a:

This signal is only a small portion of the full data, and you don’t want to store all those values. Create a subsampled version of the signal, which contains every fourth value. Plot this, against the corresponding entries of the ```time``` vector, on top of the original data (use matlab’s ```hold``` function, and plot with flag ’r*-’). How does this reduced version of the data look, compared to the original? Does it provide a good summary of the original measurements? Is the subsampling operation linear? Shift-invariant? Explain.



    
![png](Question%205%20Sampling%20and%20aliasing_files/Question%205%20Sampling%20and%20aliasing_7_0.png)
    


Response: Subsampling by keeping every fourth element results in a linear system (LS). Suppose a LS $L$ applys the subsampling such that $\vec{x} \rightarrow L \rightarrow \vec{y}$ then $L(\vec{x})=\vec{y}$. It holds true that  $L(\vec{x}) + L(\vec{x}) = L(\vec{x} + \vec{x})=2\cdot \vec{y}$ where $\vec{y}$ contains every 4th element of the input. However, it is not time invariant since $L(\vec{x} \{n-1\}) \neq \vec{y} \{n-1\}$.

How does this reduced version of the data look, compared to the original?
Response: The red lines (subsampled) follow the white lines (original) closely, showing the main ups and downs.

Does it provide a good summary of the original measurements?
Response: Yes, it provides a good summary of the original measurements.

Is the subsampling operation linear? Shift-invariant?
Response: For the linear, yes, it is linear. But for the shift-invariant, no, it is not shift-invariant.

### Part b:

Examine your EEG result in the frequency domain. First plot the magnitude (amplitude) of the Fourier transform of the original signal, over the range [􀀀N=2; (N=2) 􀀀 1] (use ```fftshift```). By convention, the ”Delta” band corresponds to frequencies less than 4Hz, ”Theta” band is 4-7Hz, ”Alpha” band 8-15Hz, and ”Beta” is 16-31Hz. For these data, which band shows the strongest signal?


    
![png](Question%205%20Sampling%20and%20aliasing_files/Question%205%20Sampling%20and%20aliasing_10_0.png)
    


By convention, the ”Delta” band corresponds to frequencies less than 4Hz, ”Theta” band is 4-7Hz, ”Alpha” band 8-15Hz, and ”Beta” is 16-31Hz. For these data, which band shows the strongest signal?
Response: The strongest signal is the Beta band.

### Part c:

Plot the Fourier magnitude for signals downsampled by factors of 2, 3, and 4, after upsampling them back to full size (i.e., make a full-size signal filled with zeros, and set every kth sample equal to one of the subsampled values, for subsampling by factor k). What is the relationship between these plots and the original frequency plot. What has happened to the frequency components of the original signal? Does the strongest signal band change?


    
![png](Question%205%20Sampling%20and%20aliasing_files/Question%205%20Sampling%20and%20aliasing_13_0.png)
    


What is the relationship between these plots and the original frequency plot. 
Response: As the subsampling factor increases, the spread of frequency components becomes wider.

What has happened to the frequency components of the original signal? 
Response: 
k=2: Frequency components look similar to the original but are spread out than k=1
k=3: Frequency components are more spread out than k=2
k=4: More spread out than k=3

Does the strongest signal band change?
Response: Yes, the strongest signal band changes.
