import random

def chromosome(courses, timeslots):

    length = courses * timeslots
    chromosome = [random.randint(0, 1) for _ in range(length)]


    if sum(chromosome) == 0:
        chromosome[random.randint(0, length - 1)] = 1

    return chromosome


def fitnessCalculation(chromosome, courses, timeslots):
#timeslot segments
    timeslots = [chromosome[i * courses:(i + 1) * courses] for i in range(timeslots)]

#overlap penalty
    overlap= 0
    for timeslot in timeslots:
        schedul = sum(timeslot)
        if schedul > 1:
            overlap+= (schedul - 1)

#consistency penalty
    scheduleCount = [0] * courses
    for timeslot in timeslots:
        for index in range(courses):
            scheduleCount[index] += timeslot[index]

    penaltyCount = sum(abs(schedule_count - 1) for schedule_count in scheduleCount)

#total fitness
    total_penalty = overlap+ penaltyCount
    return -total_penalty  # (-) penalty as fitness

def Crossover(pc1, pc2):

    length = len(pc1)
    point_1 = random.randint(1, length - 2)
    point_2 = random.randint(point_1 + 1, length - 1)

    offspring1 = pc1[:point_1] + pc2[point_1:point_2] + pc1[point_2:]
    offspring2 = pc2[:point_1] + pc1[point_1:point_2] + pc2[point_2:]

    return offspring1, offspring2, (point_1, point_2)


def main():
    input_file_path = r'C:\cse422\Lab02Text.txt' 

    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

#Parse input
        courses, timeslots = map(int, lines[0].strip().split())
        courseNames = [line.strip() for line in lines[1:courses + 1]]

        chromosome = [1, 1, 0, 1, 1, 0, 0, 1, 0]  

        fitness_value = fitnessCalculation(chromosome, courses, timeslots)

        print("Chromosome:", ''.join(map(str, chromosome)))
        print("Fitness value:", fitness_value)
#ranbdomly
        pc1 = [1, 0, 1, 0, 1, 0, 0, 1, 1] 
        pc2 = [1, 1, 0, 0, 1, 1, 0, 0, 1]  

        offspring1, offspring2, crossover_points = Crossover(pc1, pc2)

        print("\nTwo-Point Crossover:")
        print("Parent 1:", ''.join(map(str, pc1)))
        print("Parent 2:", ''.join(map(str, pc2)))
        print("Crossover Points:", crossover_points)
        print("Offspring 1:", ''.join(map(str, offspring1)))
        print("Offspring 2:", ''.join(map(str, offspring2)))

    except FileNotFoundError:
        print(f"Error: File not found at {input_file_path}. Please ensure the file exists and the path is correct.")
    except ValueError as e:
        print(f"Error: {e}. Please check the input file format.")


if __name__ == "__main__":
    main()
