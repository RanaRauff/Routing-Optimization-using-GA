import random
import fitness
# Constant Parameters

n = 4
xy = {}    # Stores coordinate in xy form
val = {}    # Stores value at coordinate

for i in range(1, n+1):
    for j in range(1, n+1):
        xy[n*i-n+j] = (i-1, j-1)
        val[(i-1, j-1)] = n*i-n+j

source = [1, 3, 5, 6]
destination = [16, 13, 16, 16]


def generate_path(source, destination):
    path = []
    path.append(source)
    d = destination
    while destination not in path:
        # print(path,path[-1])
        x = xy[path[-1]][0]
        y = xy[path[-1]][1]
        if x < xy[d][0] and y < xy[d][1]:
            path.append(random.choice([val[(x+1, y)], val[(x, y+1)]]))
        elif x > xy[d][0] and y > xy[d][1]:
            path.append(random.choice([val[(x-1, y)], val[(x, y-1)]]))
        elif x > xy[d][0] and y < xy[d][1]:
            path.append(random.choice([val[(x-1, y)], val[(x, y+1)]]))
        elif x < xy[d][0] and y > xy[d][1]:
            path.append(random.choice([val[(x+1, y)], val[(x, y-1)]]))
        elif x == xy[d][0] and y < xy[d][1]:
            path.append(val[(x, y+1)])
        elif x == xy[d][0] and y > xy[d][1]:
            path.append(val[(x, y-1)])
        elif x < xy[d][0] and y == xy[d][1]:
            path.append(val[(x+1, y)])
        elif x > xy[d][0] and y == xy[d][1]:
            path.append(val[(x-1, y)])
    return path


def initialize():
    population = []
    for _ in range(10):
        chromosome = []
        # making zipped list for source-destination pair
        l = list(zip(source, destination))
        # print("sdfs",l)
        for i in range(4):
            chromosome.append(generate_path(*l[i]))
        population.append(chromosome)
    return population


def show(population):
    for chromosome in population:
        print(chromosome)
        print('')

def alternate_population(population,fitness_list,ind):
    max_fitness=fitness_list.index(max(fitness_list)) #maximum fitness value 
    max_list=[i for i in population[ind] if max_fitness+1 in i[1:-1]]
    if not max_list:
        return population

    else:

        max_fitness_list=random.choice(max_list) #list of list having max repeated element
        altered_list=max_fitness_list[:max_fitness_list.index(max_fitness+1)-1]+generate_path(max_fitness_list[max_fitness_list.index(max_fitness+1)-1],max_fitness_list[-1])
        population[ind].remove(max_fitness_list)
        population[ind].append(altered_list)
        return population

if __name__=="__main__":
    population = initialize()
    show(population[0])

    # print(population)
    # fitness.visualize(fitness.FitnessFunction(population[0]))
    # print("adadaa",fitness.FitnessFunction(population[0]))
    fitness_list=fitness.FitnessFunction(population[0])
    fitness.visualize(fitness.FitnessFunction(population[0]))
    print(fitness_list)
    # for i in range(len(population)):
    #     population=alternate_population(population,fitness.FitnessFunction(population[i]),i)
    #     print(population)
    #     print("===============================================================")
    # print(len(population))
    populationx=alternate_population(population,fitness_list,0)[0] #the new path generated for population of index 0
    print("new population[0]",populationx)
    fitness.visualize(fitness.FitnessFunction(populationx))
        # show(pop)
