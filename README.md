# Experimention-results
We have conducted experiments in simulation on a construction game to prove the optimization of human-robot collaboration. To do this, we optimize the HRC by considering performance criteria (time completion and the number of human errors) in the cost function of the decision-making process. 

Experiment conditions:
- The human can choose one among three actions : A<sub>H,G</sub> with a probability P<sub>G</sub> = I<sub>1</sub>, A<sub>H,W</sub> with a probability P<sub>W</sub> = I<sub>2</sub>, and  A<sub>H,B</sub> with a probability P<sub>B</sub> = 1-(I<sub>1</sub> + I<sub>2</sub>).
- We tested for I<sub>1</sub> =(0:0.1:1) and I<sub>2</sub> =(0:0.1:1) except for I<sub>1</sub> = I<sub>2</sub> = 0.
- We tested the ratio between the time taking by the human do make an action t<sub>A<sub>H</sub></sub> and the one taken by the robot t<sub>A<sub>R</sub></sub> for 1:1, 1:1.5, 1:2, 1:3, 1:4, 1:5.
- We tested the number of cubes required to solve the puzzle for 2, 3, 4 and 5.
- We conducted 10000 simulations to calculate the average time and the standard variation. 
