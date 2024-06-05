# HW1

## Question 1: Testing for (non)linearity

Suppose, for each of the systems below, you observe the indicated input/output pairs of vectors (or scalars). Determine whether each system could possibly be a linear system. If so, provide an example of a matrix that is consistent with the observed input/output pairs, and state whether you think that matrix is unique (i.e., the only matrix that is consistent with the observations). If not, explain why.

System 1:
  * 1 -> [4, 6]
  * 2.5 -> [10, 14]

System 2:
  * [6, 3] −→ [12, 12]
  * [-2, -1] −→ [-6, -6]

System 3:
  * [1, 2] −→ [5, -1]
  * [1, -1] −→ [1, 4]
  * [3, 0] −→ [7, 8]

System 4:
  * [2, 4] −→ 0
  * [-2, 1] −→ 3

System 5:
  * 0 −→ [1, 2]

To be satisfied as a linear system, it needs to obey the principle of superposition: additivity and homogeneity.

**Additivity:**
  $\( F(x_1 + x_2) = F(x_1) + F(x_2) \)$

**Homogeneity:**
  $\( F(a \cdot x) = a \cdot F(x) \)$

**Or together**:
  $\( F(a \cdot x_1 + b \cdot x_2) = a \cdot F(x_1) + b \cdot F(x_2) \)$

#### System 1:
  * 1 -> [4, 6]
  * 2.5 -> [10, 14]

We have 2.5 / 1 = 2.5 so it scales 2.5 times

S(2.5 * 1)  = 2.5 * S(1)  = 2.5 * [4, 6]
            = [10, 15] != [10, 14]

==> System 1 is not linear

#### System 2
  * [6, 3] −→ [12, 12]
  * [-2, -1] −→ [-6, -6]

We have [-2, -1] / [6, 3] = -(1/3)

S((-1/3) * [6, 3]) = (-1/3) * S([6, 3]) = (-1/3) * [12, 12] = [-4, -4] != [-6, -6] 

==> System 2 is not linear

#### System 3 
  * [1, 2] −→ [5, -1]
  * [1, -1] −→ [1, 4]
  * [3, 0] −→ [7, 8]

We have [3, 0] = [1, 2] + 2[1, -1]

So S([3, 0])    = S([1, 2] + 2[1, -1])
                = S([1, 2]) + 2S([1, -1])
                = [5, -1] + 2[1, 4]
                = [7, 7] != [7, 8] 
                
==> System 3 is not linear

#### System 4 
  * [2, 4] −→ 0
  * [-2, 1] −→ 3

We have: y(1x1)  = M(1x2) * x(2x1)
 ==> 2a + 4b = 0 and -2a + b = 3
 ==> a = -6/5 and b = 3/5

==> System 4 is linear

#### System 5
  * 0 −→ [1, 2]

Take alpha = 5
S(0) = S(alpha * 0) = alpha * S(0) = 5 * [1, 2] != [1, 2]
==> System 5 is not linear system
