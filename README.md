# Experimention-results
We have conducted experiments in simulation on a construction game to prove the optimization of human-robot collaboration. To do this, we optimize the HRC by considering performance criteria (time completion and the number of human errors) in the cost function of the decision-making process. 

Experiment conditions:
- The human can choose one among three actions : A;<sub>H,G</sub> with a probability $P_G = I_1$,  $A_{H,W}$ with a probability $P_W = I_2$, and  $A_{H,B}$ with a probability $P_B = I_3 = 1-(I_1 + I_2).
- We tested for $I_1 =(0:0.1:1)$ and $I_2 =(0:0.1:1)$ except for $I_1 = I_2 = 0$.
- We tested the ratio between the time taking by the human do make an action $t_{A_H}$ and the one taken by the robot $t_{A_R}$ for 1:1, 1:1.5, 1:2, 1:3, 1:4, 1:5.
- We tested the number of cubes required to solve the puzzle for 2, 3, 4 and 5.
- We conducted 10000 simulations to calculate the average time and the standard variation. 
