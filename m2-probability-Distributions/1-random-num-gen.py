import numpy as np
y = list(range(0, 10))  ## Range 0 to 9
randomlist=np.random.choice(y,7)  
# sample n=7 observations randomly selects 7 elements from the list y.
# Each element in randomlist is a randomly picked number from the original list y.
# by default is produces 
print(randomlist)



### 1 simulation of 7 flips 
print(np.random.binomial(7, 0.2, size=1))
## 7  : number of trials/flip
## p=0.2 : Each trial has a 20% of success.
## size = 1 : only one sample is to drawn.
## output obtains 2 heads in 7 flips

n, p = 1, 0.2    ### 1 number of flips, 0.2 success probability
s = np.random.binomial(n, p, 7) ## 7 Simulations of n flips ( Simulation == experiment involving one ore more trials)
print(s)
## output is array of size 7 , with each element being the result of simulations one trial. (a single flip)
## [0 0 1 0 0 0 0]
