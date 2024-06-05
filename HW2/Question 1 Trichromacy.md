## Question 1: Trichromacy
Load the file ```colMatch.mat``` in your MATLAB environment. This file contains matrices and vectors related to the color matching experiment presented in class. In particular, the variable P is an N × 3 matrix containing wavelength spectra for three “pri- mary” lights, that could be used in a color-matching experiment. For these problems N = 31, corresponding to samples of the visible wavelength spectrum from 400nm to 700nm in increments of 10nm.

The function ```humanColorMatcher.p``` simulates a normal human observer in a color match- ing experiment. The input variable ```light``` should contain the wavelength spectrum of a test light (a 31-dimensional column vector). The variable ```primaries``` should contain the wave- length spectra of a set of primary lights (typically, a 31 × 3 matrix, as for matrix P described above). The function returns a 3-vector containing the observer’s “knob settings” - the in- tensities of each of the primaries that, when mixed together, appear identical to the test light. The function can also be called with more than one test light (by passing a matrix whose columns contain 31-dimensional test lights), in which case it returns a matrix whose columns are the knob settings corresponding to each test light.

  - (a) Create a test light with an arbitrary wavelength spectrum, by generating a random column vector with 31 positive components (use ```rand```). Use ```humanColorMatcher``` to “run an experiment”, asking the “human” to set the intensities of the three primaries in ```P``` to match the appearance of the test light. Compute the 31-dimensional wavelength spectrum of this combination of primaries, plot it together with the original light spec- trum, and explain why the two spectra are so different, even though they appear the same to the human.

  - (b) Now characterize the human observer as a linear system that maps 31-dimensional lights to 3-dimensional knob settings. Specifially, run a set of experiments to estimate the contents of a 3 × 31 color-matching matrix M that can predict the human responses. Verify on a few random test lights that this matrix exactly predicts the responses of the function ```humanColorMatcher```.

  - (c) The variable ```Cones``` contains (in the rows) approximate spectral sensitivities of the three color photoreceptors (cones) in the human eye: ```Cones(1,:)``` is for the L (long-wavelength, or red) cones, ```Cones(2,:)``` the M (green) cones, and ```Cones(3,:)``` the S (blue) cones. Applying the matrix Cones to any light $\vec{l}$ yields a 3-vector containing the average number of photons absorbed by that cone (try ```plot(Cones’```) to visualize them!). Verify that the cones provide a physiological explanation for the matching ex- periment, in that the cone absorptions are equal for any pair of lights that are perceptually matched. First, do this informally, by checking that randomly generated lights and their corresponding 3-primary matching lights produce equal cone absorptions. Then, provide a few lines of matlab code that provide a more mathematical demonstration, along with an extended comment explaining your reasoning using concepts from linear algebra. [Hints for two possible approaches: (1) write math/code that computes cone responses for any test light and then computes the weighted combination of primaries that would produce the same cone responses - show that this is numerically the same as the color-matching matrix; (2) convince yourself, and explain why, it is sufficient to show that M and Cones have the same nullspace. Then use SVD to demonstrate that this is true!]

  - (d) The function ```altHumanColorMatcher(light,primaries)``` simulates a color-deficient human observer in a standard color matching experiment. (i) for a random test light, compare the knob settings for this observer with those of the normal human. Do this for several runs of ```altHumanColorMatcher(light,primaries)```. How do they differ? (ii) Compute cone absorptions for the test light, and for the mixture of three matching primaries (by applying the ```Cones``` matrix). Do this for both the normal human observer, and for multiple runs of the abnormal observer. Try this for several different test lights. How do the cone responses of the normal and abnormal observers differ? Can you offer a diagnosis of the underlying cause of color deficiency in the abnormal observer?

### Part a:
Create a test light with an arbitrary wavelength spectrum, by generating a random column vector with 31 positive components (use ```rand```). Use ```humanColorMatcher``` to “run an experiment”, asking the “human” to set the intensities of the three primaries in ```P``` to match the appearance of the test light. Compute the 31-dimensional wavelength spectrum of this combination of primaries, plot it together with the original light spec- trum, and explain why the two spectra are so different, even though they appear the same to the human.

    [[1.1108926 ]
     [0.15554466]
     [0.40202417]]
    




    <matplotlib.legend.Legend at 0x1b35dd6e930>




    
![png](Question%201%20Trichromacy_files/Question%201%20Trichromacy_4_2.png)
    


### Part b:
Now characterize the human observer as a linear system that maps 31-dimensional lights to 3-dimensional knob settings. Specifially, run a set of experiments to estimate the contents of a 3 × 31 color-matching matrix M that can predict the human responses. Verify on a few random test lights that this matrix exactly predicts the responses of the function ```humanColorMatcher```.

    Out of 50 tests, our list called matchingMatrix got the right answer 50 times.
    

### Part c:
The variable ```Cones``` contains (in the rows) approximate spectral sensitivities of the three color photoreceptors (cones) in the human eye: ```Cones(1,:)``` is for the L (long-wavelength, or red) cones, ```Cones(2,:)``` the M (green) cones, and ```Cones(3,:)``` the S (blue) cones. Applying the matrix Cones to any light $\vec{l}$ yields a 3-vector containing the average number of photons absorbed by that cone (try ```plot(Cones’```) to visualize them!). Verify that the cones provide a physiological explanation for the matching ex- periment, in that the cone absorptions are equal for any pair of lights that are perceptually matched. First, do this informally, by checking that randomly generated lights and their corresponding 3-primary matching lights produce equal cone absorptions. Then, provide a few lines of matlab code that provide a more mathematical demonstration, along with an extended comment explaining your reasoning using concepts from linear algebra. [Hints for two possible approaches: (1) write math/code that computes cone responses for any test light and then computes the weighted combination of primaries that would produce the same cone responses - show that this is numerically the same as the color-matching matrix; (2) convince yourself, and explain why, it is sufficient to show that M and Cones have the same nullspace. Then use SVD to demonstrate that this is true!]


    When using the cones matrix with two different lights, we got results [[6.1881863 ]
     [4.73508237]
     [3.81274333]] for the first light and [[6.1881863 ]
     [4.73508237]
     [3.81274333]] for the second one. These results should be close to each other.
    Looking at the list below, we can see that it looks a lot like the matchingMatrix list we had before.
    [[ True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True]
     [ True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True]
     [ True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True  True  True  True  True  True
       True  True  True  True  True  True  True]]
    


    
![png](Question%201%20Trichromacy_files/Question%201%20Trichromacy_8_1.png)
    


### Part d:
The function ```altHumanColorMatcher(light,primaries)``` simulates a color-deficient human observer in a standard color matching experiment. (i) for a random test light, compare the knob settings for this observer with those of the normal human. Do this for several runs of ```altHumanColorMatcher(light,primaries)```. How do they differ? (ii) Compute cone absorptions for the test light, and for the mixture of three matching primaries (by applying the ```Cones``` matrix). Do this for both the normal human observer, and for multiple runs of the abnormal observer. Try this for several different test lights. How do the cone responses of the normal and abnormal observers differ? Can you offer a diagnosis of the underlying cause of color deficiency in the abnormal observer?

    How the settings on a knob change between someone who sees all colors and someone who is colorblind. 
    Test: 1
    [[1.30488953]
     [0.21155273]
     [0.25681663]]
    [[ 1.05369546]
     [-2.76463902]
     [ 3.68895121]]
     
    Test: 2
    [[0.94594124]
     [0.29952096]
     [0.45985917]]
    [[ 0.67263823]
     [-2.93862151]
     [ 4.19407445]]
     
    Test: 3
    [[ 1.58306429]
     [-0.38146065]
     [ 0.57801819]]
    [[ 1.32053124]
     [-3.49199864]
     [ 4.16508041]]
     
    Test: 4
    [[ 1.18502387]
     [ 0.33440321]
     [-0.14089952]]
    [[ 0.95147739]
     [-2.4326967 ]
     [ 3.05011102]]
     
    Test: 5
    [[0.65129381]
     [0.46861865]
     [0.16123778]]
    [[ 0.4587342 ]
     [-1.81286156]
     [ 2.79223329]]
     
    For colorblind people, the red and green settings are usually set high and are different from those who see all colors.
    

    Test: 1
    [[5.55941642]
     [5.19726192]
     [3.51783145]]
    [[5.55941642]
     [5.19726192]
     [3.51783145]]
    [[5.55941642]
     [7.2008209 ]
     [3.51783145]]
     
    Test: 2
    [[5.28673458]
     [4.82764703]
     [3.06934498]]
    [[5.28673458]
     [4.82764703]
     [3.06934498]]
    [[5.28673458]
     [7.15033885]
     [3.06934498]]
     
    Test: 3
    [[3.60339634]
     [3.24705124]
     [3.22456353]]
    [[3.60339634]
     [3.24705124]
     [3.22456353]]
    [[3.60339634]
     [5.22058338]
     [3.22456353]]
     
    Test: 4
    [[5.86167252]
     [4.62820551]
     [2.77492717]]
    [[5.86167252]
     [4.62820551]
     [2.77492717]]
    [[5.86167252]
     [6.7678381 ]
     [2.77492717]]
     
    Test: 5
    [[5.78370904]
     [5.00213839]
     [3.76226817]]
    [[5.78370904]
     [5.00213839]
     [3.76226817]]
    [[5.78370904]
     [7.53669554]
     [3.76226817]]
     
    When looking at the cone reaction, the person with the eye issue has trouble seeing green light. The reaction for the green light is much bigger than for the other colors.
    
