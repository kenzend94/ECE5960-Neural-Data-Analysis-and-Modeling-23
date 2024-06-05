## Question 4: A simple visual neuron
Suppose a retinal neuron in a particular species of toad generates responses that are a weighted sum of the (positive-valued) intensities of light that is sensed at 6 localized regions of the retina. The weight vector is [1, 3, 8, 8, 3, 1]. (a) Is this system linear? If so, how do you know? If not, provide a counterexample. (b) What unit-length stimulus vector (i.e., vector of light intensities) elicits the largest response in the neuron? Explain how you arrived at your answer. (c) What physically-realizable unit-length stimulus vector produces the smallest response in this neuron? Explain. [hint: think about the geometry by visualizing a simpler version of the problem, in 2 dimensions]

### Part a:
Is this system linear? If so, how do you know? If not, provide a counterexample.

Because the retinal neuron generates responses as a weighted sum of the inputs ==> the neuron is a linear system.

### Part b:
What unit-length stimulus vector (i.e., vector of light intensities) elicits the largest response in the neuron? Explain how you arrived at your answer.


To have max response, we should align s with w ==> elicit the maximum response is a unit-length vector in the direction of w

    Norm of w:  12.165525060596439
    Unit length vector that elicits the largest response U is:  [0.08219949 0.73979544 5.26076759 5.26076759 0.73979544 0.08219949]
    

### Part c:
What physically-realizable unit-length stimulus vector produces the smallest response in this neuron? Explain. [hint: think about the geometry by visualizing a simpler version of the problem, in 2 dimensions]

The minimal possible neuron response is 0. To get this, the stimulus vector must be orthogonal to the weight vector, satisfying the condition u·v = 0.

    Orthogonal Vector (Normalized): [ 0.9966159 -0.0203391 -0.0542376 -0.0542376 -0.0203391 -0.0067797]
    Is the orthogonal vector orthogonal to the weights vector:  True
    
