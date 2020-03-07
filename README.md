# Noisy Channel Communication Probability Demo 
Demonstration on conditional probability communication through a noisy channel. 

## 1. Probability of erroneous transmission
Consider the following experiment, where the required probabilities 𝑝𝑝0 ; 𝜀𝜀0; and 𝜀𝜀1
You transmit a one-bit message S and look at the received signal R . 
If R=S, the experiment in considered a success., otherwise it is a failure.
You repeat this experiment N = 100,000 times and count the number of failures. 
## 2. Conditional probability: P(R= 1 S= 1)
Using the same probabilities 𝑝𝑝0 ; 𝜀𝜀0; and 𝜀𝜀1 as before and consider the following
experiment:
You create and transmit a one-bit message S as you did before. The goal is to
calculate the conditional probability P(R = 1 | S = 1). This means that you will
focus only in those transmissions where S = 1.
For all the events for which the transmitted signal is S = 1, look at the received
bit R . If R = 1, the experiment is a success, i.e. success is defined as the
conditional event: (R=1 |S=1).
You repeat this experiment N=100,000 times and count the number of successes.
## 3. Conditional probability: P(S= 1 R= 1)
Use the same probabilities 𝑝𝑝0 ; 𝜀𝜀0; and 𝜀𝜀1 as before and consider the following
experiment:
You create and transmit a one-bit message S as you did before. The goal is to
calculate the conditional probability P(S = 1 | R = 1) . This means that you will
only be interested in those messages where the received signal is R = 1.
For all the events for which the received signal is R = 1, look at transmitted bit
S . If S = 1, the experiment is a success, i.e. success is defined as the conditional
event: ( 1 1)
## 4. Enhanced transmission method
Use the same probabilities 𝑝𝑝0 ; 𝜀𝜀0; and 𝜀𝜀1 as before and consider the following
experiment:
You create and transmit a one-bit message S as before. In order to improve
reliability, the same bit “S” is transmitted three times (S S S) as shown in
Figure 2.
The received bits “R” are not necessarily the same as the transmitted bits “S”
due to transmission errors. The three received bits, shown as (R1 R2 R3) in
Figure 2 will be equal to one of the following eight triplets:
(R1 R2 R3) ={ (000), (001), (010), (100), (011), (101), (110), (111) }
When you look at the received triplet (R1 R2 R3) you must decide what was the
bit “S” originally transmitted by using voting and the majority rule. Here are
some examples of the majority rule. 
