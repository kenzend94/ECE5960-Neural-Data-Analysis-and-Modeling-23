## Question 1: Bayes’ rule and eye color.
A male and female chimpanzee have blue and brown eyes, respectively. The brown-eyed allele can be denoted as a capital B, whereas the blue-eyed allele can be represented as a lowercase b. Assume a simple genetic model in which the gene for brown eyes is always dominant (so that the trait of blue eyes can only arise from two blue eyed genes, but the trait of brown eyes can arise from two brown-eyed genes, or one of each). You can also assume: i) the probability of the mother being BB is 50% and the probability of her being Bb is 50%; and ii) the a priori probability that each of the four gene configurations is equally probable. For each question, provide the math, and explain your reasoning.
  - (a) Suppose you observe that they have a single child with brown eyes. What is the probability that the female chimp has a blue-eyed gene?
  - (b) Suppose you observe that they have a second child with brown eyes. Now what is the probability?
  - (c) Generalizing, suppose they have N children with brown eyes... express the probability, as a function of N.


### Part a:
Suppose you observe that they have a single child with brown eyes. What is the probability that the female chimp has a blue-eyed gene?

Bayes’ rule:

$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

    Probability that that the female chimp has a blue-eyed gene: 0.33
    

### Part b:
Suppose you observe that they have a second child with brown eyes. Now what is the probability?

    If the mother is BB, then both children will be brown eyed
    P(Both_children_brown|BB) =  1
    
    If the mother is Bb, then each child has a 50% chance of being brown eyed
    P(Both_children_brown|Bb) = P(Child_brown|Bb) * P(Child_brown|Bb) and P(Child_brown|Bb) =  0.5
    P(Both_children_brown|Bb) =  0.5 * 0.5
    P(Both_children_brown|Bb) =  0.25
    
    probability of both children having brown eyes
    P(Both_children_brown) = P(Both_children_brown|BB) * P(BB) + P(Both_children_brown|Bb) * P(Bb)
    P(Both_children_brown) =  1 * 0.5 + 0.25 * 0.5
    P(Both_children_brown) =  0.625
    
    probability that the mother is Bb given both children have brown eyes
    P(Bb|Both_children_brown) = P(Both_children_brown|Bb) * P(Bb) / P(Both_children_brown)
    P(Bb|Both_children_brown) =  0.25 * 0.5 / 0.625
    P(Bb|Both_children_brown) =  0.2
    
    Probability that the female have a second child with brown eyes: 0.20
    

### Part c:
Generalizing, suppose they have N children with brown eyes... express the probability, as a function of N.

Let X be the event that the mother is Bb
So P(X) = 1/2
X' is the event that the mother is BB (opposite of Bb)
So P(X') = 1/2

Let Y be the event that the mother has N children have brown eyes.

And the chidlren are independent of each other.

==> So the probability of N children having brown eyes is P(Y|X) = (1/2)^N

P(Y) = P(Y|X) * P(X) + P(Y|X') * P(X')
P(Y) = (1/2)^N * (1/2) + 1 * (1/2)
P(Y) = (1/2)^N * (1/2) + 1/2

Applying Bayes' rule:
P(X|Y) = P(Y|X) * P(X) / P(Y)
P(X|Y) = 1 / ((2^N + 1)

$$ P(X|Y) = \frac{1}{2^N + 1} $$


    Testing for N = 0, 1, 2, 3
    P(X|Y) = 0.50 for N = 0
    P(X|Y) = 0.33 for N = 1
    P(X|Y) = 0.20 for N = 2
    P(X|Y) = 0.11 for N = 3
    
