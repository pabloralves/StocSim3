# Assignment 3
## An exploration of Simulated Annealing for solving the TSP with a comparison of greedy and random route initializations
### Stochastic Simulation

This repository contains all code of Assignment 3, in which we solve the TSP for three different data-sets of 51, 280 and 442 locations with simulated annealing, under random and greedy route initialization. 
Parameter tuning was performed for all investigated approaches, showing inversion and 2-Opt to be the best operators, respectively. 
Counter-intuitively, the optimal annealing settings for the smallest data-sets involved a quick cooling, converging simulated annealing to a Hill climbing optimizer.
With these parameters, results close to the optimal solutions were found with 10000 iterations, with greedy initialization having a significantly better result.
