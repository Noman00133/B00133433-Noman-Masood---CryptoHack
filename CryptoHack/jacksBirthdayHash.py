# setting value of n as 2 to the power of 11
n = 1 << 11

probability = 1
cumulative_Prob = 1

for i in range(1, n):
    # Update probability with the formula: (1-1/n)^i
    probability = pow(1 - 1/n, i)
    
    # Calculate cumulative probability
    cumulative_Prob = 1 - probability

    # Check to see if the cumulative probabilty is greater than 0.5
    if cumulative_Prob > 0.5:
        print(i) # print iteration
        break # terminate the loop
