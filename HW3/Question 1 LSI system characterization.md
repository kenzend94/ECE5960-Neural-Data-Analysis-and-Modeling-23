## Question 1: LSI system characterization
LSI system characterization. You are trying to experimentally characterize three auditory neurons, in terms of their responses to sounds. For purposes of this problem, the responses of these neurons are embodied in compiled matlab functions ```unknownSystemX.p```, (with X=1, 2, 3), each of which takes an input column vector of length N = 64 whose elements represent sound pressure over time. The response of each is a column vector (of the same length) representing the mean spike count over time. Your task is to examine them to see if they: i) behave like they are linear; and/or ii) shift-invariant; with/without iii) circular (i.e. periodic) boundary handling . For each neuron


  - (a) “Kick the tires” by measuring the response to an impulse in the first position of an input vector. Check that this impulse response is shift-invariant by comparing to the response to an impulse at positions n = 2; 4; 8. Use different n to determine how the system handles inputs near the boundary. Also check that the response to a sum of any two of these impulses is equal to the sum of their individual responses. Be sure to describe your findings.

  - (b) If the previous tests succeeded, examine the response of the system to sinusoids with frequencies $\{2\pi/N, 4\pi/N, 8\pi/N, 16\pi/N\}$, and random phases, and check whether the outputs are sinusoids of the same frequency (i.e., verify that the output vector lies completely in the subspace containing all the sinusoids of that frequency). [note: Make the input stimuli positive, by adding one to each sinusoid, and the responses should then be positive (mean spike counts)].

  - (c) If the previous tests succeeded, verify that the change in amplitude and phase from input to output is predicted by the amplitude (```abs```) and phase (```angle```) of the corresponding terms of the Fourier transform of the impulse response. If not, explain which property (linearity, or shift-invariance, or both) seems to be missing from the system. If so, do you think that the combination of all tests guarantees that the system is linear and shift-invariant? What combination of tests would provide such a guarantee?




### Part a:

“Kick the tires” by measuring the response to an impulse in the first position of an input vector. Check that this impulse response is shift-invariant by comparing to the response to an impulse at positions n = 2; 4; 8. Use different n to determine how the system handles inputs near the boundary. Also check that the response to a sum of any two of these impulses is equal to the sum of their individual responses. Be sure to describe your findings.

    System 1 is linear.
    System 1 is not shift-invariant.
    System 1 does not have circular boundary handling.
    
    System 2 is linear.
    System 2 is shift-invariant.
    System 2 has circular boundary handling.
    
    System 3 is non-linear.
    System 3 is shift-invariant.
    System 3 has circular boundary handling.
    

### Part b:

If the previous tests succeeded, examine the response of the system to sinusoids with frequencies $\{2\pi/N, 4\pi/N, 8\pi/N, 16\pi/N\}$, and random phases, and check whether the outputs are sinusoids of the same frequency (i.e., verify that the output vector lies completely in the subspace containing all the sinusoids of that frequency). [note: Make the input stimuli positive, by adding one to each sinusoid, and the responses should then be positive (mean spike counts)].

    Neuron 1, Frequency 0.10: Output does not lie in the same subspace.
    Neuron 1, Frequency 0.20: Output does not lie in the same subspace.
    Neuron 1, Frequency 0.39: Output does not lie in the same subspace.
    Neuron 1, Frequency 0.79: Output does not lie in the same subspace.
    
    Neuron 2, Frequency 0.10: Output does not lie in the same subspace.
    Neuron 2, Frequency 0.20: Output does not lie in the same subspace.
    Neuron 2, Frequency 0.39: Output does not lie in the same subspace.
    Neuron 2, Frequency 0.79: Output does not lie in the same subspace.
    
    Neuron 3, Frequency 0.10: Output does not lie in the same subspace.
    Neuron 3, Frequency 0.20: Output does not lie in the same subspace.
    Neuron 3, Frequency 0.39: Output does not lie in the same subspace.
    Neuron 3, Frequency 0.79: Output does not lie in the same subspace.
    

### Part c:

If the previous tests succeeded, verify that the change in amplitude and phase from input to output is predicted by the amplitude (```abs```) and phase (```angle```) of the corresponding terms of the Fourier transform of the impulse response. If not, explain which property (linearity, or shift-invariance, or both) seems to be missing from the system. If so, do you think that the combination of all tests guarantees that the system is linear and shift-invariant? What combination of tests would provide such a guarantee?

    Neuron 1 does not have circular boundary handling.
    Neuron 2 doesn't follow the expected amplitude and phase based on its initial response.
    Neuron 3 doesn't follow the expected amplitude and phase based on its initial response.
    

If the system's output doesn't match what we expect based on its initial response, it's not behaving consistently.

- If the system doesn't keep the same amplitude, it's not linear.
- If the system doesn't keep the same phase, it's not shift-invariant.
- If the system doesn't keep the same circular boundary handling, it's not shift-invariant.

To get the guarantees that the system is linear and shift-invariant, we need to do frequency-domain tests (checking amplitude and phase relationships with the Fourier-transformed impulse response).

