## Question 5: Gram-Schmidt
A classic method for constructing an orthonormal basis is known as Gram- Schmidt orthogonalization. First, one generates an arbitrary unit vector (e.g., by normalizing a vector created with ```randn```). Each subsequent basis vector is created by generating another arbitrary vector, subtracting off the projections of that vector along each of the previously created basis vectors, and normalizing the remaining vector.

Write a MATLAB function ```gramSchmidt``` that takes a single argument, N , specifying the dimensionality of the basis. It should then generate an N ×N matrix whose columns contain

a set of orthogonal normalized unit vectors. Try your function for N = 3, and plot the basis vectors (you can use MATLAB’s ```rotate3d``` to interactively examine these). Check your function numerically by calling it for an N larger than 3 and verifying that the resulting matrix is orthonormal. Extra credit: make your function recursive – instead of using a ```for``` loop, have the function call itself, each time adding a new column to the matrix of previ- ously created orthogonal columns. To do this, you’ll probably need to write two functions (a main function that initializes the problem, and a helper function that is called with a matrix containing the current set of orthogonal columns and adds a new column until the number of column equals the number of rows).

    Print Gram-Schmidt: 
    Print random vector: 
     [[0.73 0.99 0.49]
     [0.21 0.48 0.22]
     [0.35 0.91 0.83]]
    Print orthogonal vector:  [array([0.73, 0.99, 0.49]), array([-0.09659917,  0.06420113,  0.01420056]), array([-0.04337807, -0.14384566,  0.35525142])]
    
    Print normalized vector:  [array([0.55134002, 0.74770769, 0.37007755]), array([-0.826666  ,  0.54941354,  0.12152402]), array([-0.11246117, -0.37293158,  0.9210182 ])]
    
    
    Are the vectors orthonormal? True
    Plotting the vectors: 
    


    
![png](Question%205%20Gram-Schmidt_files/Question%205%20Gram-Schmidt_2_1.png)
    

