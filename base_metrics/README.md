##  A Priori, Guidelines 

1.  Each model is given the exact same amount of information about the rules
2.  The state of the board is clearly defined in the given prompt
3.  Prior knowledge about chess is not required to find the correct solution
4.  Trusting the expert model upon which the LLM is being graded on
5.  LLM answer is not boolean, all of the answers can be put on the spectrum

## Related Assumptions for the Importance of the Benchmark 

6.  The rules of chess are equivalent to the body of law in importance and way of prompting
7.  Board state is company's current state of the problem and is presented as such
8.  Legal chess move is corresponding to a legally compliant action suggested by LLM
9.  Halucinations and illegal moves are breaching the law which was presented to AI
10. Rating of the move relates to ability for outputing optimal compliance strategy

## Metrics of Measurment for LLM Decision

1. Base, accuracy of the taken move given all the informations from the **A priori, guidelines**
    * Level A: Response validity through syntax evaluation:
        - is it a chess move that can be parsed
        - if so does it have a proper format
    * Level B: Legal move compliance:
        - presented move is a rule based one 
        - are there any hallucinations
    * Level C: Strategic quality:
        - assigning the grade based on the expert model
        - how reliably LLM reaches Level C

2. Bias, building prompt upon the differences in how the law is formulated in different countries
    * Document format coming from a particual country (style rules):
        - does it still reach the same level from the base metric
        - is it repeating the same move that was presented by it prior
        - if above is not true, has the expert model grade changed
    * Linguistic differences between law (translation):
        - repeating the sample problems from the *Documents* section

## Solutions for Pitfalls of Existing Benchmarks

1. Memorization over reasoning, the parrot problem:
    - Forcing reasoning by creating prompt with *A Priori, Guidelines*: 3
    - Providing the base knowledge according to *A Priori, Guidelines*: 1 - 2

2. Lack of a Ground Truth, open ended tasks:
    - Using a clear grading system provided by expert models *A Priori, Guidelines*: 4
    - Allowing for variation that is not subjective *A Priori, Guidelines*: 5

3. Disconnect from Real-World Task:
    - Rule based evaluation metric for rule based domain *Realated Assumptions*: 6 - 10
    - Adaptation skills to the different law systems *Realated Assumptions*: 6 - 10

## Questions on possible improvement

1. Control Group:
    - is it suitable for our research to create one
    - if so should it be human based or LLM based

2. Checking the Vector of Hallucination
    - what are the properties of the hallucination to recognize it
    - if we know the vecors of the correct answer (Biggest Grade)
    - compare how close the hallucination answer was to correct vectors