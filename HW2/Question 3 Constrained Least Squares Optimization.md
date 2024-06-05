## Question 3: Constrained Least Squares Optimization
Load the file ```constrainedLS.mat``` into MATLAB. This contains an N × 2 data matrix, data, whose columns correspond to horizontal and vertical coordinates of a set of 2D data points, $\vec{d}_n$. It also contains a 2-vector w. Consider a constrained optimization problem:


$\min_{\vec{v}} \sum_n \left(\vec{v}^\top \vec{d}_n\right)^2, \quad \text{s.t.} \quad \vec{v}^\top \vec{w} = 1.$

Thus, the constraint on $\vec{v}$ is that it must lie on a line, perpendicular to $\vec{w}$ , whose perpendicular distance from the origin is $1/\|\vec{w}\|$.

  - (a) Rewrite the optimization problem in matrix form. Then rewrite the problem in terms of a new optimization variable, $\tilde{v}$ (a linear transformation of $\vec{v}$), such that the quantity to be minimized is now $\|\vec{\tilde{v}}\|^2$. Note: you must also rewrite the constraint in terms of $\tilde{v}$.

  - (b) The transformed problem is one that you should be able to solve. In particular, you must find the shortest vector $\tilde{v}$ that lies on the constraint line. Compute the solution for $\tilde{v}$, and plot the solution vector, the constraint line and the transformed data points.

  - (c) Transform the solution back into the original space (i.e., solve for $\vec{v}$). Plot $\vec{v}$, the original constraint line, and the original data points. Is the optimal vector $\vec{v}$ perpendicular to the constraint line? On the same graph, plot the total least squares solution (i.e., the vector that minimizes the same objective function, but that is constrained to be a unit vector). Are the two solutions the same?



\begin{align*}
\text{minimize } & \sum_n \left( \bar{v}^T \bar{d_n} \right)^2 \\
\text{subject to: } & \bar{v}^T \bar{w} = 1
\end{align*}

### Part a: 
Rewrite the optimization problem in matrix form. Then rewrite the problem in terms of a new optimization variable, $\tilde{v}$ (a linear transformation of $\vec{v}$), such that the quantity to be minimized is now $\|\vec{\tilde{v}}\|^2$. Note: you must also rewrite the constraint in terms of $\tilde{v}$.

The function:
\begin{align*}
(v^T D)^2 &= (v^T D)(D^T v) \\
&= (v^T D)(v^T D)^T \\
\bar{v} &= v^T D \\
\bar{v}^2 &= v v^T
\end{align*}


\begin{align*}
\bar{v} &= v^T D
\end{align*}

the transpose of \begin{align*} \bar{v} \end{align*} is:


\begin{align*}
\bar{v}^T &= D^T v
\end{align*}

Thus, the constraint in terms of \begin{align*} \bar{v}  \end{align*}becomes:
\begin{align*}
D^T v \bar{w} &= 1
\end{align*}

### Part b:
The transformed problem is one that you should be able to solve. In particular, you must find the shortest vector $\tilde{v}$ that lies on the constraint line. Compute the solution for $\tilde{v}$, and plot the solution vector, the constraint line and the transformed data points.


    [-0.3782429   2.01995981]
    


    
![png](Question%203%20Constrained%20Least%20Squares%20Optimization_files/Question%203%20Constrained%20Least%20Squares%20Optimization_7_1.png)
    


### Part c:
Transform the solution back into the original space (i.e., solve for $\vec{v}$). Plot $\vec{v}$, the original constraint line, and the original data points. Is the optimal vector $\vec{v}$ perpendicular to the constraint line? On the same graph, plot the total least squares solution (i.e., the vector that minimizes the same objective function, but that is constrained to be a unit vector). Are the two solutions the same?

    The optimal vector is perpendicular to the constraint line due to the dot product: [1.]
    The Least Squares Solution and the optimal solution are not the same because of the constraint.
    


    
![png](Question%203%20Constrained%20Least%20Squares%20Optimization_files/Question%203%20Constrained%20Least%20Squares%20Optimization_9_1.png)
    

