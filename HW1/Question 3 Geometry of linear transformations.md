## Question 3: Geometry of linear transformations
  - (a) Write a function ```plotVec2``` that takes as an argument a matrix of height 2, and plots each column vector from this matrix on 2-dimensional axes. It should check that the matrix argument has height two, signaling an error if not. Vectors should be plotted as a line from the origin to the vector position, using circle or other symbol to denote the “head” (see help for function ’plot’). It should also draw the x and y axes, extending from -1 to 1. The two axes should be equal size, so that horizontal units are equal to vertical units (read the help for the function ’axis’).

  - (b) Write a second function ```vecLenAngle``` that takes two vectors as arguments and returns the length (magnitude, or Euclidean-norm, not dimensionality) of each vector, as well as the angle between them. Decide how you would like to handle cases when one (or both) vectors have zero length.

  - (c) Generate a random 2x2 matrix M , and decompose it using the SVD, $M = USV^T$ . Now examine the action of this sequence of transformations on the two “standard basis” vectors, $\{\hat{e}_1, \hat{e}_2\}$. Specifically, use ```vecLenAngle``` to examine the lengths and angle between two basis vectors $\hat{e}_n$, the two vectors $V^T\hat{e}_n$, the two vectors $SV^T\hat{e}_n$, and the two vectors $USV^T\hat{e}_n$. Do these values change, and if so, after which transformation? Verify this is consistent with their visual appearance by plotting each pair using ```plotVec2```.

  - (d) Generate a data matrix $P$ with 65 columns containing 2-dimensional unit-vectors $\hat{u}_n = [\cos(\theta_n); \sin(\theta_n)]$, and $\theta_n = \frac{2\pi n}{64}, n = 0, 1, \ldots, 64$. [Hint: Don’t use a ```for``` loop! Create a vector containing the values of θn. ] Plot a single blue curve through these points, and a red star (asterisk) at the location of the first point. Consider the action of the matrix $M$ from the previous problem on this set of points. In particular, apply the SVD transformations one at a time to full set of points (again, think of a way to do this without using a for loop!), plot them, and describe what geometric changes you see (and why).


### Part a: 
Write a function ```plotVec2``` that takes as an argument a matrix of height 2, and plots each column vector from this matrix on 2-dimensional axes. It should check that the matrix argument has height two, signaling an error if not. Vectors should be plotted as a line from the origin to the vector position, using circle or other symbol to denote the “head” (see help for function ’plot’). It should also draw the x and y axes, extending from -1 to 1. The two axes should be equal size, so that horizontal units are equal to vertical units (read the help for the function ’axis’).

    Print matrix:  [[ 0.5 -0.7]
     [ 0.3  0.9]]
    


    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_3_1.png)
    


    
    Print wrong_matrix not height of 2:  [[1], [2], [3]]
    Should print error message:
    The input matrix:  [[1]
     [2]
     [3]] must have a height of 2.
    

### Part b:
Write a second function ```vecLenAngle``` that takes two vectors as arguments and returns the length (magnitude, or Euclidean-norm, not dimensionality) of each vector, as well as the angle between them. Decide how you would like to handle cases when one (or both) vectors have zero length.

    (1.0, 1.0, 90.0)
    No angle possible since there is a vector of magnitude zero, Vec1 Mag: 1.0, Vec2 Mag: 0.0
    (1.4142135623730951, 1.0, 90.0)
    

### Part c:
Generate a random 2x2 matrix M , and decompose it using the SVD, $M = USV^T$ . Now examine the action of this sequence of transformations on the two “standard basis” vectors, $\{\hat{e}_1, \hat{e}_2\}$. Specifically, use ```vecLenAngle``` to examine the lengths and angle between two basis vectors $\hat{e}_n$, the two vectors $V^T\hat{e}_n$, the two vectors $SV^T\hat{e}_n$, and the two vectors $USV^T\hat{e}_n$. Do these values change, and if so, after which transformation? Verify this is consistent with their visual appearance by plotting each pair using ```plotVec2```.

    (1.0, 1.0, 90.0)
    (1.0, 1.0, 90.0)
    (0.8147257538647885, 0.8428570300705804, 22.13850379828472)
    (0.8147257538647883, 0.8428570300705803, 22.13850379828472)
    


    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_7_1.png)
    



    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_7_2.png)
    



    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_7_3.png)
    



    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_7_4.png)
    


### Part d:
Generate a data matrix $P$ with 65 columns containing 2-dimensional unit-vectors $\hat{u}_n = [\cos(\theta_n); \sin(\theta_n)]$, and $\theta_n = \frac{2\pi n}{64}, n = 0, 1, \ldots, 64$. [Hint: Don’t use a ```for``` loop! Create a vector containing the values of θn. ] Plot a single blue curve through these points, and a red star (asterisk) at the location of the first point. Consider the action of the matrix $M$ from the previous problem on this set of points. In particular, apply the SVD transformations one at a time to full set of points (again, think of a way to do this without using a for loop!), plot them, and describe what geometric changes you see (and why).




    <matplotlib.legend.Legend at 0x1fb0c232090>




    
![png](Question%203%20Geometry%20of%20linear%20transformations_files/Question%203%20Geometry%20of%20linear%20transformations_9_1.png)
    

