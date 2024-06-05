## Question 3: Gabor filter
The response properties of neurons in primary visual cortex (area V1) are often described using linear filters. We’ll examine a one-dimensional cross-section of the most common choice, known as a “Gabor filter” (named after Electrical Engineer/Physicist Denis Gabor, who developed it in 1946 for use in signal processing)

  - (a) Create a one-dimensional linear filter that is a product of a Gaussian and a sinusoid $exp(-\frac{n^{2}}{2\sigma ^{2}})cos(\omega n)$ with parameters σ = 3.5 and ω = 2π ∗ 10/64 samples. The filter should contain 25 samples, and the Gaussian should be centered on the middle (13th) sample. Plot the filter to verify that it looks like what you’d expect. Plot the amplitude of the Fourier transform of this filter, sampled at 64 locations (MATLAB’s fft function takes an optional additional argument). What kind of filter is this? Why does it have this shape, and how is the shape related to the choice of parameters (σ, ω)? Specifically, how does the Fourier amplitude change if you alter each of these parameters?

  - (b) If you were to convolve this filter with sinusoids of different frequencies, which of them would produce a response with the largest amplitude? Obtain this answer by reasoning about the equation defining the filter (above), and also by finding the maximum of the computed Fourier amplitudes (using the ```max``` function), and verify that the answers are the same. Compute the period of this sinusoid, measured in units of sample spacing (hint: this is the inverse of its frequency, in cycles/sample), and verify by eye that this is roughly matched to the oscillations in the graph of the filter itself. Which two sinusoids would produce responses with about 25% of this maximal amplitude?

  - (c) Create three unit-amplitude 64-sample sinusoidal signals at the three frequencies (low, mid, high) that you found in part (b). Convolve the filter with each, and verify that the amplitude of the response is approximately consistent with the answers you gave in part (b). (hint: to estimate amplitude, you’ll either need to project the response onto sine and cosine of the appropriate frequency, or compute the DFT of the response and measure the ampitude at the appropriate frequency).


### Part a:
Create a one-dimensional linear filter that is a product of a Gaussian and a sinusoid $exp(-\frac{n^{2}}{2\sigma ^{2}})cos(\omega n)$ with parameters σ = 3.5 and ω = 2π ∗ 10/64 samples. The filter should contain 25 samples, and the Gaussian should be centered on the middle (13th) sample. Plot the filter to verify that it looks like what you’d expect. Plot the amplitude of the Fourier transform of this filter, sampled at 64 locations (MATLAB’s fft function takes an optional additional argument). What kind of filter is this? Why does it have this shape, and how is the shape related to the choice of parameters (σ, ω)? Specifically, how does the Fourier amplitude change if you alter each of these parameters?


    
![png](Question%203%20Gabor%20filter_files/Question%203%20Gabor%20filter_3_0.png)
    


### Part b:
If you were to convolve this filter with sinusoids of different frequencies, which of them would produce a response with the largest amplitude? Obtain this answer by reasoning about the equation defining the filter (above), and also by finding the maximum of the computed Fourier amplitudes (using the max function), and verify that the answers are the same. Compute the period of this sinusoid, measured in units of sample spacing (hint: this is the inverse of its frequency, in cycles/sample), and verify by eye that this is roughly matched to the oscillations in the graph of the filter itself. Which two sinusoids would produce responses with about 25% of this maximal amplitude?

    Expected max frequency from the filter's equation: 0.9817477042468103
    Actual max occurs at frequency: [-9.81747704  9.81747704]
    The amplitude at these frequencies is: 4.384431016503207
    Period of the sinusoid (measured in units of sample spacing): 1.0185916357881302
    Frequencies with ~25% of the max amplitude: [-14.72621556  -4.90873852   4.90873852  14.72621556]
    Expected Frequencies from reasoning: f1 = 0.9817477042468103, f2 = 0.4908738521234052, f2_1 = 1.4726215563702154
    

### Part c:

Create three unit-amplitude 64-sample sinusoidal signals at the three frequencies (low, mid, high) that you found in part (b). Convolve the filter with each, and verify that the amplitude of the response is approximately consistent with the answers you gave in part (b). (hint: to estimate amplitude, you’ll either need to project the response onto sine and cosine of the appropriate frequency, or compute the DFT of the response and measure the ampitude at the appropriate frequency).


    
![png](Question%203%20Gabor%20filter_files/Question%203%20Gabor%20filter_7_0.png)
    

