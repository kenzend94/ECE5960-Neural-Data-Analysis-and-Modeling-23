## Question 4: Analyzing and simulating experimental data. 

An international coffee conglomerate recruits you to characterize the neuropsychology underlying their customers’ adoration of pumpkin spice. You devise a blood-oxygen level dependent (BOLD) FMRI pilot experiment in which you present one of two classes of odorants to an individual while monitoring the activity of three key voxels located in the amygdala, a structure known to be associated with emotional responses. The file ```experimentData.mat``` contains: a (N × 3) matrix ```data```, where each row is the BOLD response of the three voxels on a given trial relative to some baseline; and a (N × 1) vector ```trialConds``` indicating the experimental condition of each trial. Condition 1 are trials in which you present an odorant selected randomly from a library of possible control odorants, and condition 2 are trials in which the trade secret pumpkin spice odorant is presented.

  - (a) Before doing anything quantitative with your data, it is always good practice to visualize it. First, determine how many trials of each trial condition were completed. Display this information as a 2-bin histogram with each bin representing each of the two possible trial conditions, and their heights representing their respective trial counts. Next, plot a 3D scatter plot of the recorded responses, with each point color-coded according to its associated trial condition (use the function ```scatter3``` in Matlab and be sure to label your axes). Describe your data qualitatively using this figure. Is there a noticeable difference between the two trial conditions? What geometric shape are these ’response clouds’, and what distribution would you use to model them?

  - (b) Quantify the response statistics of each individual trial condition. Calculate the means of each response cloud, as well as their respective covariance matrices. Compute the covariance matrices of each response cloud using matrix multiplication (remember to center the data first). Verify your calculation is correct by comparing with the output given by the ```cov``` function. How do the covariance matrices compare (are they similar at all or wildly different)?

  - (c) Next, compute the SVD of each covariance matrix. Plot the three singular vectors originating from the center of each response cloud and scale their amplitude by the square root of the singular values. Relative to how similar the covariance matrices were be-fore computing their SVD, how do each trial condition’s respective set of singular val-ues compare? Describe what this tells us about the relationship between the two trial conditions and, more fundamentally, the relationship between the three voxels across conditions.

  - (d) A powerful method to validate a model is by generating(i.e. simulating) new data matching your quantitative description of the real data, and then comparing them with real data. Create a function ```simResponses = odorExperiment(numTrials1,numTrials2)``` where ```numTrials1``` and ```numTrials2``` are the number of trials in a simulated experiment for condition 1 and 2, respectively. ```simResponses``` is a (N×3) matrix containing simulated responses of each of your 3 voxels during N = ```numTrials1``` + ```numTrials2``` trials. [Hint: use ```ndRandnfrom``` the previous problem]. Plot the simulated and real responses in the same figure (use subplots if you wish) to compare the two. Is your simulated response data a good characterization of the real amygdala voxel responses?

    Size of data:  (612, 3)
    Size of trialConds:  (612, 1)
    

### Part a:

Before doing anything quantitative with your data, it is always good practice to visualize it. First, determine how many trials of each trial condition were completed. Display this information as a 2-bin histogram with each bin representing each of the two possible trial conditions, and their heights representing their respective trial counts. Next, plot a 3D scatter plot of the recorded responses, with each point color-coded according to its associated trial condition (use the function ```scatter3``` in Matlab and be sure to label your axes). Describe your data qualitatively using this figure. Is there a noticeable difference between the two trial conditions? What geometric shape are these ’response clouds’, and what distribution would you use to model them?


    
![png](Question%204%20Analyzing%20and%20simulating%20experimental%20data_files/Question%204%20Analyzing%20and%20simulating%20experimental%20data_4_0.png)
    



    
![png](Question%204%20Analyzing%20and%20simulating%20experimental%20data_files/Question%204%20Analyzing%20and%20simulating%20experimental%20data_4_1.png)
    


Q: Describe your data qualitatively using this figure. Is there a noticeable difference between the two trial conditions? 
A: The blue and red points appear to be in distinct clusters ==> there is a difference in BOLD responses between the two conditions.

Q: What geometric shape are these ’response clouds’, and what distribution would you use to model them?
A: The response clouds appear to be ellipsoids. I would use a multivariate Gaussian distribution to model them.



### Part b:
Quantify the response statistics of each individual trial condition. Calculate the means of each response cloud, as well as their respective covariance matrices. Compute the covariance matrices of each response cloud using matrix multiplication (remember to center the data first). Verify your calculation is correct by comparing with the output given by the ```cov``` function. How do the covariance matrices compare (are they similar at all or wildly different)?

    Mean for Condition 1: [2.97707955 4.24881879 4.97436515]
    Mean for Condition 2: [ 9.98186089 12.08375561 11.07413275]
    
    Covariance Matrix for Condition 1:
     [[26.13151392  9.8203437   4.90869037]
     [ 9.8203437  15.74570991  3.40750737]
     [ 4.90869037  3.40750737  3.3829186 ]]
    Covariance Matrix for Condition 2:
     [[12.90381388  8.09733134  2.91064268]
     [ 8.09733134 26.94541895  6.31922585]
     [ 2.91064268  6.31922585  4.42510768]]
    
    Covariance Matrix for Condition 1 (using cov function):
     [[26.13151392  9.8203437   4.90869037]
     [ 9.8203437  15.74570991  3.40750737]
     [ 4.90869037  3.40750737  3.3829186 ]]
    Covariance Matrix for Condition 2 (using cov function):
     [[12.90381388  8.09733134  2.91064268]
     [ 8.09733134 26.94541895  6.31922585]
     [ 2.91064268  6.31922585  4.42510768]]
    
    Using np.close to compare two matrices
    Are the two covariance matrices for Condition 1 the same? True
    Are the two covariance matrices for Condition 2 the same? True
    

Q: How do the covariance matrices compare (are they similar at all or wildly different)?

A: The covariance matrices are similar. They are not wildly different.


### Part c:

Next, compute the SVD of each covariance matrix. Plot the three singular vectors originating from the center of each response cloud and scale their amplitude by the square root of the singular values.  Relative to how similar the covariance matrices were be-fore computing their SVD, how do each trial condition’s respective set of singular val-ues compare?  Describe what this tells us about the relationship between the two trial conditions and, more fundamentally, the relationship between the three voxels across conditions.

    np.sqrt(S1) [5.76529617 3.13819526 1.47418895]
    np.sqrt(S2) [5.68979005 3.03438501 1.6410781 ]
    V1 [[-0.83831231  0.5263743  -0.14199494]
     [-0.50877926 -0.84890989 -0.14316309]
     [-0.19589829 -0.0477713   0.97945993]]
    V2 [[-0.40319898  0.90923937 -0.10351013]
     [-0.88265474 -0.41626017 -0.21828442]
     [-0.24155994  0.00335165  0.97038011]]
    


    
![png](Question%204%20Analyzing%20and%20simulating%20experimental%20data_files/Question%204%20Analyzing%20and%20simulating%20experimental%20data_11_1.png)
    



    
![png](Question%204%20Analyzing%20and%20simulating%20experimental%20data_files/Question%204%20Analyzing%20and%20simulating%20experimental%20data_11_2.png)
    


Q: Relative to how similar the covariance matrices were before computing their SVD, how do each trial condition’s respective set of singular values compare?
A: The singular values for Condition 1 are much larger than those for Condition 2.
Q: Describe what this tells us about the relationship between the two trial conditions and, more fundamentally, the relationship between the three voxels across conditions.



### Part d:

A powerful method to validate a model is by generating(i.e. simulating) new data matching your quantitative description of the real data, and then comparing them with real data. Create a function ```simResponses = odorExperiment(numTrials1,numTrials2)``` where ```numTrials1``` and ```numTrials2``` are the number of trials in a simulated experiment for condition 1 and 2, respectively. ```simResponses``` is a (N×3) matrix containing simulated responses of each of your 3 voxels during N = ```numTrials1``` + ```numTrials2``` trials. [Hint: use ```ndRandnfrom``` the previous problem]. Plot the simulated and real responses in the same figure (use subplots if you wish) to compare the two. Is your simulated response data a good characterization of the real amygdala voxel responses?

    responses_cond2 (312, 3)
    simResponses (612, 3)
    


    
![png](Question%204%20Analyzing%20and%20simulating%20experimental%20data_files/Question%204%20Analyzing%20and%20simulating%20experimental%20data_14_1.png)
    

