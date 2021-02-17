import numpy
from numpy import mean
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from tabulate import tabulate

def human_choice(Human_intelligence_1, Human_intelligence_2):
    probability_distribution = [Human_intelligence_1, Human_intelligence_2, 1 - (Human_intelligence_1 + Human_intelligence_2)] #should be the same length than the human action's number
    return numpy.random.choice(numpy.arange(0, len(Human_actions)), p=probability_distribution)

def method1(index_H_action): #robot choice with C_3
    index_R_action = Payoff_method1_Robot_actions[0+index_H_action*len(Human_actions):index_H_action*len(Human_actions)+len(Human_actions)].index(max(Payoff_method1_Robot_actions[0+index_H_action*len(Human_actions):index_H_action*len(Human_actions)+len(Human_actions)]))
    return index_R_action

def method2(index_H_action): #robot choice with C_1
    index_R_action = Payoff_method2_Robot_actions[0+index_H_action*len(Human_actions):index_H_action*len(Human_actions)+len(Human_actions)].index(max(Payoff_method2_Robot_actions[0+index_H_action*len(Human_actions):index_H_action*len(Human_actions)+len(Human_actions)]))
    return index_R_action

def global_cost (I1, I2): # t_C (equation 15)
    cost_method1 = (I1*(time_human_actions[0]+time_robot_actions[1])+I2*(time_human_actions[1]+time_robot_actions[0])+(1-(I1 + I2))*(time_human_actions[2]+time_robot_actions[2])) / (I1+I2) 
    cost_method2 = (I1*(time_human_actions[0]+time_robot_actions[0])+I2*(time_human_actions[1]+time_robot_actions[0])+(1-(I1 + I2))*(time_human_actions[2]+time_robot_actions[2])) / (I1*2+I2) 
    return round(cost_method1, 4), round(cost_method2, 4)

# Game datas
# Payoff_method1_Robot_actions = utilities calculated by equation 12 for C_3 and Payoff_method2_Robot_actions = utilities calculated by equation 12 for C_1
Human_actions = ["AH1", "AH2", "AH3"] 
Payoff_Human_actions = [540, 0, -540]
time_human_actions = [15, 0, 15]
Robot_actions = ["AR1", "AR2", "AR3"]
time_robot_actions = [75, 0, 75]
Payoff_method1_Robot_actions = [-108, 0, -108,  108, 0, -108, -108, 0, 108]
Payoff_method2_Robot_actions = [108, 0, -108,  108, 0, -108, -108, 0, 108]
cubes = 4
number_of_simulation = 10000

#initialisation of variables
H_actions = []
cubes_placed = 0
total_time = 0
Human_intelligence_1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] #I_1
Human_intelligence_2 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] #I_2
I1 = 0
I2 = 0
i = 0
total_time_method1 = []
total_time_method2 = []
Human_intelligence = []
mean_time_1 = []
std_time_1 = []
min_time_1 = []
max_time_1 = []
min_time_2 = []
max_time_2 = []
mean_time_2 = []
std_time_2 = []
figure_I1 = []
figure_I2 = []


while I1 < len(Human_intelligence_1):
    while I2 < len(Human_intelligence_2):
        print ("I1 : ", Human_intelligence_1[I1], "I2 : ", Human_intelligence_2[I2])         
        if (Human_intelligence_1[I1] != 0) or (Human_intelligence_2[I2] != 0):
            cost_method1, cost_method2 = global_cost(Human_intelligence_1[I1], Human_intelligence_2[I2]) # calculating t_C_1 and  t_C_2 
            print ("cost_method : ",cost_method1, cost_method2)
            figure_I1.append(Human_intelligence_1[I1])
            figure_I2.append(Human_intelligence_2[I2])
            Human_intelligence.append("I1 : " + str(Human_intelligence_1[I1]) + " and I2 : " + str(Human_intelligence_2[I2]))
            while i < number_of_simulation:
                 # Simulation of the Game for C_3
                while cubes_placed < cubes:
                    index_H_action =  human_choice(Human_intelligence_1[I1], Human_intelligence_2[I2])
                    H_actions.append(Human_actions[index_H_action])
                    total_time += time_human_actions[index_H_action]
                    if index_H_action == 0:
                        cubes_placed += 1

                    if cubes_placed == cubes:
                        break
                    else:
                        if cost_method1 < cost_method2: 
                            index_R_action = method1(index_H_action)
                        elif cost_method1 >= cost_method2: # equilibrium : both methods are equivalent
                            index_R_action = method2(index_H_action)
                        total_time += time_robot_actions[index_R_action]
                        if index_R_action == 0:
                            cubes_placed += 1

                # print ("total time with method 1 : ", total_time)
                total_time_method1.append(total_time)

                #re-initialisation of variables
                cubes_placed = 0
                total_time = 0
                iter = 0

                # Simulation of the Game for C_1
                while cubes_placed < cubes:
                    if iter < len(H_actions):
                        index_H_action = Human_actions.index(H_actions[iter]) 
                    else: 
                        index_H_action =  human_choice(Human_intelligence_1[I1], Human_intelligence_2[I2])
                    # index_H_action =  human_choice(Human_intelligence_1[I1], Human_intelligence_2[I2])
                    iter += 1
                    total_time += time_human_actions[index_H_action]
                    if index_H_action == 0:
                        cubes_placed += 1

                    if cubes_placed == cubes:
                        break
                    else:
                        index_R_action = method2(index_H_action)
                        total_time += time_robot_actions[index_R_action]
                        if index_R_action == 0:
                            cubes_placed += 1

                total_time_method2.append(total_time)

                #re-initialisation of variables
                total_time = 0
                cubes_placed = 0
                H_actions = []

                i += 1

            mean_time_1.append(mean(total_time_method1))
            std_time_1.append(numpy.std(total_time_method1))
            mean_time_2.append(mean(total_time_method2))
            std_time_2.append(numpy.std(total_time_method2))
            min_time_1.append(min(total_time_method1))
            max_time_1.append(max(total_time_method1))
            min_time_2.append(min(total_time_method2))
            max_time_2.append(max(total_time_method2))
            total_time_method1 = []
            total_time_method2 = []
            i = 0    
        I2 += 1
    Human_intelligence_2.pop()
    I2 = 0
    I1 += 1

improvement = []
zip_object = zip(mean_time_2, mean_time_1)
for list1_i, list2_i in zip_object:
    improvement.append(((list1_i-list2_i)/list1_i)*100)

###############################
#printing and registring the datas in a table
i = 0
table = []
row = ["I1 and I2", "average time with C3", "average time with C1", "improvement", "std of time with C3", "std of time with C1", "maximum time with C3", "minimum time with C3", "maximum time with C1", "minimum time with C1"]
table.append(row)

while  i < len(Human_intelligence):
    row  = [Human_intelligence[i], mean_time_1[i], mean_time_2[i], improvement[i], std_time_1[i], std_time_2[i], max_time_1[i], min_time_1[i], max_time_2[i], min_time_2[i]]
    i += 1
    table.append(row)

with open('results.txt', 'w') as f:
    f.write("%s\n" %tabulate(table, tablefmt="grid"))

#####################################
# Difference between the average output time (seconds) 2D figure with the varation of I2 with respect to I1
i = 0 
j = 0
list_I2 = []
plt.figure(figsize=(25,12))
matplotlib.rc('font', size=15)
plt.grid(True)
while (j < len(figure_I1)):
    if (round(figure_I1[j], 2) == i):
        list_I2.append(figure_I2[j])
        j += 1
    else:
        difference = []
        zip_object = zip(mean_time_2[j-len(list_I2):j], mean_time_1[j-len(list_I2):j])
        for list1_i, list2_i in zip_object:
            difference.append(list1_i-list2_i)

        plt.plot(list_I2, difference,'-o')
        plt.annotate('I1 = ' + str(i), xy= (list_I2[len(list_I2)-1], difference[len(difference)-1]), xytext=(list_I2[len(list_I2)-1]+0.05, difference[len(difference)-1]+0), arrowprops=dict())
        plt.xlabel('Values of I2')
        plt.ylabel('Difference between the average output time (seconds) obtained by case 1 and 3 over 10000 simulations')
        
        list_I2 = []
        i += 0.1 # step to change I_1
        i = round(i, 2)
plt.plot(0, mean_time_2[len(mean_time_2)-1] - mean_time_1[len(mean_time_1)-1],'-o')
plt.annotate('I1 = ' + str(1), xy= (0, mean_time_2[len(mean_time_2)-1] - mean_time_1[len(mean_time_1)-1]), xytext=(0.05, mean_time_2[len(mean_time_2)-1] - mean_time_1[len(mean_time_1)-1]), arrowprops=dict())
plt.savefig("fig1.png", bbox_inches='tight', pad_inches=0.5)

####################################
# Difference between the average output time (seconds) 3D figure
fig = plt.figure(figsize=(25,12))
ax = plt.axes(projection='3d')

X = figure_I1
Y = figure_I2
Z = []
zip_object = zip(mean_time_2, mean_time_1)
for list1_i, list2_i in zip_object:
    Z.append(list1_i-list2_i)

ax.scatter3D(X, Y, Z, c=Z)
ax.set_xlabel('x : I1')
ax.set_ylabel('y : I2')
ax.set_zlabel('z : mean time with method 2 - mean time with method 1 (sec)')
plt.savefig("fig2.png", bbox_inches='tight', pad_inches=0.5)
plt.show()

#################################
# Percentage of time improvement 2D figure with the varation of I2 with respect to I1
i = 0 
j = 0
list_I2 = []
plt.figure(figsize=(25,12))
matplotlib.rc('font', size=20)
plt.grid(True)
while (j < len(figure_I1)):
    if (round(figure_I1[j], 2) == i):
        list_I2.append(figure_I2[j])
        j += 1
    else:
        difference = []
        zip_object = zip(mean_time_2[j-len(list_I2):j], mean_time_1[j-len(list_I2):j])
        for list1_i, list2_i in zip_object:
            difference.append(((list1_i-list2_i)/list1_i)*100)

        plt.plot(list_I2, difference,'-o')
        plt.annotate('I1 = ' + str(i), xy= (list_I2[len(list_I2)-1], difference[len(difference)-1]), xytext=(list_I2[len(list_I2)-1]+0.05, difference[len(difference)-1]+0), arrowprops=dict())
        plt.xlabel('Values of I2')
        plt.ylabel('Percentage of the time improvement')  

        list_I2 = []
        i += 0.1 # step to change I_1
        i = round(i, 2)
plt.plot(0, improvement[len(improvement)-1],'-o')
plt.annotate('I1 = ' + str(1), xy= (0, improvement[len(improvement)-1]), xytext=(0.05, improvement[len(improvement)-1]), arrowprops=dict())
plt.savefig("fig3.png", bbox_inches='tight', pad_inches=0.5)

################################
#Percentage of time improvement 3D figure 

Z = []
zip_object = zip(mean_time_2, mean_time_1)
for list1_i, list2_i in zip_object:
    Z.append(((list1_i-list2_i)/list1_i)*100)

ax.scatter3D(X, Y, Z, c=Z)
ax.set_xlabel('x : I1')
ax.set_ylabel('y : I2')
ax.set_zlabel('z : Percentage of the time improvement')
plt.savefig("fig4.png", bbox_inches='tight', pad_inches=0.5)
plt.show()