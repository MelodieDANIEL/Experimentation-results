# Experimentation-results
We have conducted experiments in simulation on a construction game to prove the optimization of Human-Robot Collaboration (HRC). To do this, we optimize the HRC by considering performance metrics (time completion and the number of human errors) in the reward values of the utility function of the decision-making process. 

Experiment conditions:
- The human can choose one among three actions : A<sub>H,G</sub> with a probability P(A<sub>H,G</sub>) = I<sub>1</sub>, A<sub>H,W</sub> with a probability P(A<sub>H,W</sub>) = I<sub>2</sub>, and  A<sub>H,B</sub> with a probability P(A<sub>H,B</sub>) = 1-(I<sub>1</sub> + I<sub>2</sub>).
- We tested for I<sub>1</sub> =(0:0.1:1) and I<sub>2</sub> =(0:0.1:1) except for I<sub>1</sub> = I<sub>2</sub> = 0.
- We tested the ratio between the time taking by the human do make an action t<sub>A<sub>H</sub></sub> and the one taken by the robot t<sub>A<sub>R</sub></sub> for 1:1, 1:1.5, 1:2, 1:3, 1:4, 1:5.
- We tested the number of cubes required to solve the puzzle for 2, 3, 4, and 5.
- We conducted 10000 simulations to calculate the average time and the standard variation. 

Experiment parameters:
experiment parameters are written in the file "experiment_parameters.txt".


Experiment resulting data:
For each experiment, we got the following data:
- A Table ("results.txt") that contains the average time (in seconds) calculated, among 10000 simulations, for the C<sub>3</sub> (our utility function) and the one for C<sub>1</sub> (state-of-the-art utility function). We calculated the percentage improvement of the time for C<sub>3</sub> in comparaison of the C<sub>1</sub>. It contains also the standard variation, the maximum value and the minimum one for the C<sub>3</sub> and the C<sub>1</sub>.
- "Figure 1": a 2D figure that presents the difference between the average output time (in seconds) obtained by case 1 and 3 over 10000 simulations.
- "Figure 2": a 3D figure that presents the difference between the average output time (in seconds) obtained by case 1 and 3 over 10000 simulations.
- "Figure 3": a 2D figure that presents the percentage of the time improvement.
- "Figure 4": a 3D figure that presents the percentage of the time improvement.
