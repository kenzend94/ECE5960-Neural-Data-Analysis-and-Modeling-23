## Question 2: Convolution in MATLAB

Convolution in matlab. Suppose you have a linear shift-invariant system with impulse response r = [4 2 1 0.5]
Because it is LSI, the response of this system to any input vector in can be computed as a convolution.

  - (a) Compute responses to the eight 8-dimensional impulse vectors, using MATLAB’s ```conv``` function: ```out = conv(in, r)```. How do these compare to what you’d expect from output 2 the convolution formula given in class, $y(n) = \sum_k r(n-k) x(k)$? Specifically, compute the matrix that represents the linear system. What is the size, and organization of this matrix?

  - (b) How does MATLAB’s ```conv``` function handle boundaries?
  - (c) Using ```conv```, compute the response to an input vector of length 48 containing a single cycle cosine. Is this a single-cycle sinusoid? Why or why not? If not, what modification is necessary to the ```conv``` function to ensure that it will behave according to the “sine-in, sine-out” behavior we expect of LSI systems?


### Part a:
Compute responses to the eight 8-dimensional impulse vectors, using MATLAB’s ```conv``` function: ```out = conv(in, r)```. How do these compare to what you’d expect from output 2 the convolution formula given in class, $y(n) = \sum_k r(n-k) x(k)$? Specifically, compute the matrix that represents the linear system. What is the size, and organization of this matrix?

    Response to impulse vector 1: [4.  2.  1.  0.5 0.  0.  0.  0.  0.  0.  0. ]
    Response to impulse vector 2: [0.  4.  2.  1.  0.5 0.  0.  0.  0.  0.  0. ]
    Response to impulse vector 3: [0.  0.  4.  2.  1.  0.5 0.  0.  0.  0.  0. ]
    Response to impulse vector 4: [0.  0.  0.  4.  2.  1.  0.5 0.  0.  0.  0. ]
    Response to impulse vector 5: [0.  0.  0.  0.  4.  2.  1.  0.5 0.  0.  0. ]
    Response to impulse vector 6: [0.  0.  0.  0.  0.  4.  2.  1.  0.5 0.  0. ]
    Response to impulse vector 7: [0.  0.  0.  0.  0.  0.  4.  2.  1.  0.5 0. ]
    Response to impulse vector 8: [0.  0.  0.  0.  0.  0.  0.  4.  2.  1.  0.5]
    
    Matrix representation of the LSI system:
    [[4.  2.  1.  0.5 0.  0.  0.  0.  0.  0.  0. ]
     [0.  4.  2.  1.  0.5 0.  0.  0.  0.  0.  0. ]
     [0.  0.  4.  2.  1.  0.5 0.  0.  0.  0.  0. ]
     [0.  0.  0.  4.  2.  1.  0.5 0.  0.  0.  0. ]
     [0.  0.  0.  0.  4.  2.  1.  0.5 0.  0.  0. ]
     [0.  0.  0.  0.  0.  4.  2.  1.  0.5 0.  0. ]
     [0.  0.  0.  0.  0.  0.  4.  2.  1.  0.5 0. ]
     [0.  0.  0.  0.  0.  0.  0.  4.  2.  1.  0.5]]
    

### Part b:
How does MATLAB’s ```conv``` function handle boundaries?

When MATLAB's conv function convolves two signals, it does extend their lengths by padding with zeros.

For example, given two signals:

a = [1, 2, 3]
b = [0.5, 1.5]

When we convolve them, it gonna extended like this:

a = [0, 1, 2, 3, 0]
b = [0, 0.5, 1.5, 0, 0]


The output of the convolution will be = length(a) + length(b) - 1 = 3 + 2 - 1 = 4 






    result  = [0.5 2.5 4.5 4.5]
    

### Part c:
Using ```conv```, compute the response to an input vector of length 48 containing a single cycle cosine. Is this a single-cycle sinusoid? Why or why not? If not, what modification is necessary to the ```conv``` function to ensure that it will behave according to the “sine-in, sine-out” behavior we expect of LSI systems?


    
![png](Question%202%20Convolution%20in%20matlab_files/Question%202%20Convolution%20in%20matlab_9_0.png)
    


    Length of the response: 51
    

Is this a single-cycle sinusoid? Why or why not?

Based on the convolution with the provided impulse response r, the output is not a single-cycle sinusoid. The output is a sinusoid with a period of 48, which is 4 times the period of the original signal.

This is because the impulse response is a 4-point signal, and the convolution of the original signal with the impulse response is equivalent to the sum of 4 shifted copies of the original signal.

 If not, what modification is necessary to the conv function to ensure that it will behave according to the “sinein,
sine-out” behavior we expect of LSI systems?

To get "sine-in, sine-out" behavior, the impulse response should be a delta function. In other words, the impulse response should be a single 1 followed by zeros. This will result in a convolution that is equivalent to the original signal.

