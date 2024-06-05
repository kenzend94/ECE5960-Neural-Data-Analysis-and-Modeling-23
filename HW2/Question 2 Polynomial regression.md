## Question 2: Polynomial regression
Load the file ```regress1.mat``` into your MATLAB environment. Plot variable Y as a function of X. Find a least-squares fit of the data with polynomials of order 0 (a constant), 1 (a line, parameterized by intercept and and slope), 2, 3, 4, and 5. [Compute this using ```svd``` and basic linear algebra manipulations that you’ve learned in class!] On a separate graph, plot the squared error as a function of the order of the polynomial. Which fit do you think is “best”? Explain.


    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_2_0.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_0.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_1.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_2.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_3.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_4.png)
    



    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_4_5.png)
    


    Errors: 
    [109.23483667634054, 108.96598920027574, 20.50016077846658, 8.29315235432474, 4.797360875225383, 4.65014897910382]
    


    
![png](Question%202%20Polynomial%20regression_files/Question%202%20Polynomial%20regression_5_1.png)
    


By looking at the graph and errors data, there is a sharp decrease in error from degree 2 to 3, and then a gradual decrease from degree 3 to 6, but the decrease is not much. From degree 5 to 6, the reduction in error is very small. 

So, we can say that the best polynomial degree is 5 because it has the lowest error and the error does not decrease much after that. And also degree 5 gives a good balance between the error and polynomial degree.
