## Question 6: Null and Range spaces
Load the file ```mtxExamples.mat``` into your MATLAB world. You’ll find a set of matrices named mtxN, with N = 1, 2.... For each matrix, use the SVD to: (a) determine if there are non-trivial (i.e., non-zero) vectors in the input space that the matrix maps to zero (i.e., determine if there’s a nullspace). If so, write a MATLAB expression that generates a random example of such a vector, and verify that the matrix maps it to the zero vector; (b) write a MATLAB expression to generate a random vector y that lies in the range space of the matrix, and then verify that it’s in the range space by finding an input vector, x, such that $Mx = y$.

    Matrix rank is 2 and shape is (3, 2), making it no null space
    Matrix 1 * our solution = [-0.25422039 -0.6049933  -0.50729637] which is ≈ random vector [-0.25422039 -0.6049933  -0.50729637]
    
    
    Matrix rank is 1 and shape is (3, 3), making it has a null space
    Matrix2 multiplied by the random vector is [1.13450915e-15 4.60785923e-17 9.17235038e-17] which is ~zero
    Matrix 2 * our solution = [-0.25945825 -0.01051115 -0.02097492] which is ≈ random vector [-0.25945825 -0.01051115 -0.02097492]
    
    
    Matrix rank is 2 and shape is (2, 3), making it no null space
    Matrix3 multiplied by the random vector is [ 0.00000000e+00 -1.73472348e-16] which is ~zero
    Matrix 3 * our solution = [-1.29945991  0.1834207 ] which is ≈ random vector [-1.29945991  0.1834207 ]
    
    
    Matrix rank is 1 and shape is (2, 2), making it has a null space
    Matrix4 multiplied by the random vector is [8.8817842e-16 4.4408921e-16] which is ~zero
    Matrix 4 * our solution = [-1.38630313 -0.56545489] which is ≈ random vector [-1.38630313 -0.56545489]
    
