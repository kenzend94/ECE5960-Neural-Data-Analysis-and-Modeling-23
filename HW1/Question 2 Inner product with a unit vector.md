## Question 2: Inner product with a unit vector.
Given unit vector $\hat{u}$, and an arbitrary vector $\vec{v}$, write (MATLAB) expressions for computing:

  - (a) the component of $\vec{v}$ lying along the direction $\hat{u}$,

  - (b) the component of $\vec{v}$ that is orthogonal (perpendicular) to $\hat{u}$, and

  - (c) the distance from $\vec{v}$ to the component that lies along direction $\hat{u}$.

Now convince yourself your code is working by testing it on random vectors $\hat{u}$ and $\vec{v}$ (generate these using ```randn```, and don’t forget to re-scale $\hat{u}$ so that it has unit length). First, do this visually with 2-dimensional vectors, by plotting $\hat{u}$, $\vec{v}$, and the two components described in (a) and (b). (hint: execute ”axis equal” to ensure that the horizontal and vertical axes have the same units). Then test it numerically in higher dimensions (e.g., 4) by writing (and running) expressions to verify each of the following:

  - the vector in (a) lies along the same line (i.e., points in the same or opposite direction) as $\hat{u}$.

  - the vector in (a) is orthogonal to the vector in (b).

  - the sum of the vectors in (a) and (b) is equal to $\vec{v}$.

  - the sum of squared lengths of the vectors in (a) and (b) is equal to $\|\vec{v}\|^2$.

### Part a: the vector in (a) lies along the same line (i.e., points in the same or opposite direction) as $\hat{u}$

$$
\vec{v}_{proj} = (\vec{v} \cdot \hat{u}) \hat{u}
$$

    [3 0 0]
    

### Part b: the vector in (a) is orthogonal to the vector in (b).

$$
\vec{v}_{rej} = \vec{v}-\vec{v}_{proj}
$$

    [0 4 5]
    

### Part c: the sum of the vectors in (a) and (b) is equal to $\vec{v}$.

$$
\left| \vec{v}_{rej} \right| = \sqrt{\sum{v_{rej_i}^2}}
$$

    6.4031242374328485
    

### Part d: the sum of squared lengths of the vectors in (a) and (b) is equal to $\|\vec{v}\|^2$.

**Testing Inner Product Functions**

* Functions for creating randomized vectors

    [0.68561546 0.28102284]
    [0.69445054 0.71954045]
    

    u = [0.7829899  0.62203442]
    
    v = [0.66273246 0.41829927]
    
    proj_u_v = [0.61003476 0.48463284]
    
    orthogonal_comp = [ 0.0526977  -0.06633357]
    
    


    
![png](Question%202%20Inner%20product%20with%20a%20unit%20vector_files/Question%202%20Inner%20product%20with%20a%20unit%20vector_15_1.png)
    


* Functions for higher dimensional testing

    Is the vector in (a) lies along the same line (i.e., points in the same or opposite direction) as u:  True
    Is the vector in (a) is orthogonal to the vector in (b):  True
    Is the sum of the vectors in (a) and (b) is equal to v:  True
    Is the sum of the squared lengths of the projection and orthogonal component is equal to the squared length of v:  True
    
