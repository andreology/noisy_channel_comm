#Andre Barajas
#Spring 2020
#Use the following probabilities provided by Dr. Zhou, for this project:
#where p0=0.6   ;   e0=0.05;   e1=0.03
import numpy as np
import random

#function to create one bit of the transmitted message "S". Where p1 = 1-p
def nSidedDie(p, p1):
    n = 2
    parray = np.array([p, p1])
    csum = np.cumsum(parray)
    cparray = np.append(0, csum)
    random = np.random.rand()

    for index in range (0, n):
        if random > cparray[index] and random <= cparray[index + 1]:
            result = index + 1
    return result

#1. Probability of erroneous transmission
#Simulating number of failures from transimitted message S
def erroneous_transmission(trials, p, e0, e1):
    failure_count = 0
    r = 0

    for index in range(0, trials):
        #assign random # to s bit message
        s = nSidedDie(p, 1 - p) - 1
        if s == 1:
          r = nSidedDie(e1, 1 - e1) - 1
        else:
          r = nSidedDie(1 - e0, e0) - 1
        #if failure occurs, increase counter
        if r != s:
            failure_count += 1
    print("probability of an incorrect transmission error: ", failure_count / trials)

#2. Conditional Probability: P(R = 1 | S = 1)
#Simulating number of successful received messages given that S = 1
def successful_receive(trials, p, e0, e1):
    signal_count = 0
    received_count_success = 0
    r = 0
    for i in range(0, trials):
        s = nSidedDie(p, 1 - p) - 1
        #check successful conditional probability
        if s == 1:
            signal_count += 1
            r = nSidedDie(e1, 1 - e1) - 1
            if r == 1:
              received_count_success += 1
    #probablity = success / sample space
    print("probability that R = 1 given that S = 1: ",
    received_count_success / signal_count)

#3. Conditional Probability: P(S = 1 | R = 1)
#Simulating number of successful sent messages given that R = 1
def successful_send(trials, p, e0, e1):
    signal_count_success = 0
    received_count = 0
    r = 0

    for i in range(0, trials):
        s = nSidedDie(p, 1 - p) - 1

        if s == 1:
          r = nSidedDie(e1, 1 - e1) - 1
        else:
          r = nSidedDie(1 - e0, e0) - 1
        #only focused on times where r = 1
        if r == 1:
            received_count += 1
            if s == 1:
                signal_count_success += 1
    #probablity = success / sample space
    print("probability that S = 1 given that R = 1: ",
    signal_count_success / received_count)

#4. Enhanced transmission method
#Simulating the transmission of bit S being received and decoded incorrectly
def received_decoded(trials, p, e0, e1):
    received_decoded_bad = 0
    success_count = 0
    bit_decode = -1

    #lists to store received and signals
    received_bits = []
    signal_bits = []


    for i in range(0, trials):
         s = nSidedDie(p, 1 - p) - 1
         signal_bits = [s, s, s]

         if 1 in signal_bits:
              received_bits = [nSidedDie(e1, 1 - e1)-1, nSidedDie(e1, 1 - e1) - 1,nSidedDie(e1, 1 - e1) -1 ]

         if 0 in signal_bits:
              received_bits = [nSidedDie(1-e0, e0)-1, nSidedDie(1 - e0, e0) - 1, nSidedDie(1-e0, e0) - 1]
         received_decoded_bad = np.sum(received_bits)

         if received_decoded_bad >= 2:
             bit_decode = 1
         else:
             bit_decode = 0
         if bit_decode != s:
             success_count += 1
    print("probablity that bit S is received and decoded incorrectly: ",
    success_count / trials)

def main():
    #values provided by Dr. Zhou
    p0 = 0.6
    e0 = 0.05
    e1 = 0.03
    N = 100000
    print("1")
    erroneous_transmission(N, p0, e0, e1)
    print("2")
    successful_receive(N, p0, e0, e1)
    print("3")
    successful_send(N, p0, e0, e1)
    print("4")
    received_decoded(N, p0, e0, e1)

if __name__ == "__main__":
 main()
