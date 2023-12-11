# Stoc Sim 3

**Due date**:  Thursday 21st December

**Overleaf link**: https://www.overleaf.com/project/6571ed26196307d20452f284

## Tasks
**Next meeting**: Monday 11/12, 17h

**Meeting date**: 8/12 (Pablo, Juan)

**Meeting date**: 7/12 (Pablo, Jasper, Juan)

### GROUP
- [ ] Read intro & methods together (Monday 11/12)

### PABLO
- [X] Create ReadMe
- [X] Report: Intro (7/12)
- [X] Report: Methods: text and understanding (8/12)
- [X] Improve Jasper's code
- [X] Learn how to properly do stat testing (10/12 w/ Juan)
- [ ] Review additional stat testing (10/12)
- [ ] Add confidence interval to code -> several runs conf. of score (11/12)

### JASPER
- [ ] Review Stoc Book
- [X] Find best data structure for the soluton (numpy?)
- [X] First working code
- [X] Implement simulated annealing and several mutation functions

 ### JUAN
- [X] Report: Research and understand annealing 
- [X] Report: Methods: 3 algorithms (11/12). No information was found, added brief description.
- [X] Report: Annealing algorthm (11/12)
- [ ] Stat testing: find how to add T-Test, U-Test... (11/12)


## Rules
Let others know what you are going to code BEFORE you start! Here.



## Method


### Things to measure/test
1. Check if optimal solution is reached (and if so, stop sim)
  *IDEA:* To check if a good local minimum is reached, set a range of acceptable scores above the optimal as a function of starting score and then check if convergence has a low enough score to be considered good
3. Iterations needed until reaching optimal solution (w/ certain confidence)
4. "Try different cooling schedules and observe their effects on convergence" Compare average score of different methods/parameters like the initial temperature, (because methods convrege at different speed) -> Heatmap
5. Compare average time of different methods/parameters
6. Effects of Markov Chain’s length on the convergence. -> number of iterations...
7. Average score after random initialization (by doing several random initializations)
8. T-Test?
9. U-Test?
10. Welch?
11. H0?
12. Sample variance: when testing a method, we will have different starting points. There is a chance that some methods will be very sensitive to the starting conditions. If a method is insensitive to starting conditions it will converge at roughly same number of iterations and thus its "total simulation iterations needed" will have a smaller sample variance (also test H0). Therefore by measuring sample variance of the agregated results for each method can measure how sensitive our method was to innitial conditions.
13. Confidence interval of mean
14. Conf. interval of average best score of method -> compare parameters to see which gets closer to optimal
15. Is score as function of iterations a certain distribution (namely, exponential decay)?
16.  make statements, e.g. on the expected value or variance of the simulated system ?

### Things to set
1. N: number of runs
2. n: Number of iterations
3. nmax: Maximum number of iterations (sometimes we won't reach optimal solution)
4. optimal_solution: optimal solution provided to us, used as stopping criteria
5. Parameters of annealing
6. Whether or not we random initialize each run or not -> we think we should, *"The same starting route (shuffle) can have differential impact for different methods. To avoid this bias, we need to shuffle each starting route for each run, despite fixing all other parameters"*

#### IDEA 1. Find parameters (number of simulations & iterations/sim) in the literature:
<!--- This paper is very old, so we use significantly more iterations (epochs) than is done here, while still having significantly less computation time. I don't see what information can be useful but i might very well have missed it. In that case please enlighten me :-)
-->
1. https://repository.lib.ncsu.edu/bitstream/handle/1840.4/5622/1983_0094.pdf?sequence=1
2. https://www.sciencedirect.com/science/article/abs/pii/S0743731596901215
3. https://link.springer.com/chapter/10.1007/0-387-28356-0_7
4. For stopping criteria -> np.exp((current_score - new_score) / T < threshold -> no variation from it to next
5. For stopping criteria RUNNING AVERAGE -> np.exp((running average) / T <  threshold -> no variation in many iterations
5. For parameters literature and try a big range -> find threshold values after which it is pointless to test (if t0 is too low it will not converge, if it is too high big compt time)

#### IDEA 2. Use Stopping Algorithm to find optimal number of runs (Algorithm 1 of Lecture 3)
It would be like the one in our last assignments
