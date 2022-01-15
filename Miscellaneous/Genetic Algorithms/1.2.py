

import random
import matplotlib.pyplot as plt

def generatePopulation():
    for i in range(populationSize):
        temp = []
        for j in range(chromosomeLength):
            temp.append(random.randint(0,1))
        population.append(temp)

def fitness(lst):
    temp = 0
    for i in range(len(lst)):
        temp = temp + (2**i)*lst[i]
    return temp


def select():
    rouletteLine = [0]
    for chromosome in population:
        rouletteLine.append(rouletteLine[-1] + fitness(chromosome)/((2**20-1)*populationSize))

    num = random.uniform(0,1)

    for i in range(populationSize-1):
        if rouletteLine[i] < num and num < rouletteLine[i+1]:
            break
    return population[i]

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.uniform(0,1) < mutationRate:
            if chromosome[i] == 0:
                chromosome[i] = 1
            else:
                chromosome[i] = 0

def crossOver(chromo1,chromo2):
    if random.uniform(0,1) < crossoverRate:
        locus = random.randint(0,chromosomeLength-1)
        offspring1 = chromo1[:locus+1] + chromo2[locus+1:]
        offspring2 = chromo1[locus+1:] + chromo2[:locus+1]
    else:
        offspring1 = chromo1
        offspring2 = chromo2
    mutate(offspring1)
    mutate(offspring2)

    return [offspring1,offspring2]

def maxFitness():
    temp = 0
    for chromosome in population:
        if fitness(chromosome) > temp:
            temp = fitness(chromosome)
    return temp

def averageFitness():
    temp = 0
    for chromosome in population:
        temp = temp + fitness(chromosome)
    return temp/populationSize

populationSize = 100
chromosomeLength = 20
crossoverRate = 0.7
mutationRate = 0.001


population = []
newPopulation = []

generatePopulation()
#print(0,"\t",averageFitness(),"\t",maxFitness())
x_axis = []
y_axis = []
y1_axis = []

for k in range(1,100):
    for i in range(round(populationSize/2)):
        parent1 = select()
        parent2 = select()
        newPopulation.append(crossOver(parent1,parent2)[0])
        newPopulation.append(crossOver(parent1,parent2)[1])

    population = newPopulation[:]
    newPopulation.clear()
    #print(k,"\t",averageFitness(),"\t",maxFitness())
    x_axis.append(k)
    y_axis.append(averageFitness())
    y1_axis.append(maxFitness())

plt.plot(x_axis,y_axis,label = "Average fitness")
plt.plot(x_axis,y1_axis,label = "Maximum fitness")
plt.legend()
plt.show()
