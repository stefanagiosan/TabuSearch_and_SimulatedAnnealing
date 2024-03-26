import copy
import random


class TabuSearch:
    def __init__(self, filename):
        self.__objects = []
        self.__max_weight = 0
        self.__nr_objects = 0

        self.__configuration_file = filename

    def __configuration_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.__nr_objects = len(lines[0])

            lines = [line.strip() for line in lines if line.strip()]
            for line in lines[1:-1]:
                entity = line.split()
                object_number = int(entity[0])
                weight = int(entity[1])
                value = int(entity[2])

                self.__objects.append({"nr": object_number, "weight": weight, "value": value})

            self.__max_weight = int(lines[-1])

    #this method evaluates the value of a solution for the knapsack problem, each item has a weight and a value
    #and there is a constraint of the maximum weight that can be carried
    def __evaluate(self, solution):
        total_weight = 0
        total_value = 0
        for i in range(len(solution)):
            if solution[i] == 1:
                total_weight += self.__objects[i]["weight"]
                total_value += self.__objects[i]["value"]

        if total_weight <= self.__max_weight:
            return total_value
        return 0

    #this method generates a random solution, where each item is represented either by "0" or by "1".
    #0 means the item is not included, 1 means it is included. The decision to include is made randomly
    def __generate(self):
        solution = []
        for _ in range(len(self.__objects)):
            choice = random.choice([0, 1])
            solution.append(choice)
        return solution

    # this method generates the neighbours of a solution. Each neighbour si obtained by flipping the value.
    @staticmethod
    def __generate_neighbours(solution):
        neighbours = []
        for i in range(len(solution)):
            sol_copy = copy.deepcopy(solution)
            sol_copy[i] = 1 - sol_copy[i]
            neighbours.append(sol_copy)
        return neighbours

    def tabu_search(self, max_iterations, tabu_iterations):
        current_solution = self.__generate()
        current_solution_eval = self.__evaluate(current_solution)
        tabu_list = []

        for _ in range(max_iterations):
            best_neighbour = None
            best_neighbour_eval = 0
            neighbours = self.__generate_neighbours(current_solution)
            nr = 0

            for neighbour in neighbours:
                if neighbour not in tabu_list:
                    neighbour_eval = self.__evaluate(neighbour)
                    if neighbour_eval > best_neighbour_eval:
                        nr = 1
                        best_neighbour = neighbour
                        best_neighbour_eval = neighbour_eval

            if nr == 1:
                current_solution = best_neighbour
                current_solution_eval = best_neighbour_eval
                tabu_list.append(best_neighbour)

                if len(tabu_list) > tabu_iterations:
                    tabu_list.pop(0)

        return current_solution_eval

