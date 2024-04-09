import random
import copy


class TabuSearch:
    def __init__(self, filename, iterations, tabu_iterations):
        self.__iterations = iterations
        self.__tabu_iterations = tabu_iterations

        self.__objects = []
        self.__max_weight = 0
        self.__nr_objects = 0

        self.__configuration_file(filename)

    def __configuration_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.__nr_objects = int(lines[0])

            lines = [line.strip() for line in lines if line.strip()]

            for line in lines[1:-1]:
                parts = line.split()
                object_id = int(parts[0])
                value = int(parts[1])
                weight = int(parts[2])
                self.__objects.append({"id": object_id, "weight": weight, "value": value})

            self.__max_weight = int(lines[-1])

    # this method evaluates the value of a solution for the knapsack problem, each item has a weight and a value
    # and there is a constraint of the maximum weight that can be carried
    def __evaluate(self, solution):
        total_weight = 0
        total_value = 0
        for i in range(0, len(solution)):
            if solution[i] == 1:
                total_weight += self.__objects[i]["weight"]
                total_value += self.__objects[i]["value"]

        if total_weight <= self.__max_weight:
            return total_value
        return 0

    # this method generates a random solution, where each item is represented either by "0" or by "1".
    # 0 means the item is not included, 1 means it is included. The decision to include is made randomly
    def __generate(self):
        solution = []
        for _ in range(len(self.__objects)):
            choice = random.choice([0, 1])
            solution.append(choice)
        return solution

    def search(self):
        solution = self.__generate()
        solution_quality = self.__evaluate(solution)
        memory = []

        for _ in range(self.__iterations):
            best_neighbour = None
            best_neighbour_quality = 0
            neighbours = self.__generate_neighbours(solution)
            found = False

            for neighbour in neighbours:
                if neighbour not in memory:
                    neighbour_quality = self.__evaluate(neighbour)
                    if neighbour_quality > best_neighbour_quality:
                        found = True
                        best_neighbour = neighbour
                        best_neighbour_quality = neighbour_quality

            if found is True:
                solution_quality = best_neighbour_quality
                solution = best_neighbour
                memory.append(best_neighbour)

                if len(memory) > self.__tabu_iterations:
                    memory.pop(0)

        return solution_quality

    # this method generates the neighbours of a solution. Each neighbour si obtained by flipping the value.
    @staticmethod
    def __generate_neighbours(solution):
        neighbours = []
        for i in range(len(solution)):
            solution_copy = copy.deepcopy(solution)
            solution_copy[i] = 1 - solution_copy[i]
            neighbours.append(solution_copy)
        return neighbours
