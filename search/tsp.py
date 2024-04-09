import math
import random

class TSP:
    def __init__(self, filename, iterations, tabu_iterations):
        self.__iterations = iterations
        self.__tabu_iterations = tabu_iterations
        self.__cities = []
        self.__nr_cities = 0

        self.__configuration_file(filename)

    def __configuration_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.__nr_cities = int(lines[0])

            lines = [line.strip() for line in lines if line.strip()]

            for line in lines[1:]:
                parts = line.split()
                city_id = int(parts[0])
                city_x = int(parts[1])
                city_y = int(parts[2])

                self.__cities.append({"id": city_id, "city_x": city_x, "city_y": city_y})

    #This method calculates the total cost of the given route by summing the distance between consecutive
    #cities using the '__get_city_distance' method
    def __evaluate(self, route):
        total_cost = 0
        for i in range(len(route) - 1):
            total_cost += self.__get_city_distance(route[i], route[i + 1])

        total_cost += self.__get_city_distance(route[-1], route[0])

        return total_cost
    #The matrix keeps track of tabu status for pairs of cities to form the initial solution. 'current route' is randomly initialized
    #as a list of cities to form the initial solution and the cost of the initial solution is calculated. The algorithm runs for a specified
    #number of iterations. The algorithm generates a neighbour and two random cities are selected. it calculates the cost of the neighbour
    #solution. If it's not tabu and it improved the current solution , the current solution is updated and the move is recorded as
    #tabu in the memory. The cost of the best solution found is returned.

    def search(self):
        memory = [[0] * self.__nr_cities for _ in range(self.__nr_cities)]

        current_route = list(range(self.__nr_cities))
        random.shuffle(current_route)
        cost_current_route = self.__evaluate(current_route)

        for _ in range(self.__iterations):
            neighbour = self.generate_neighbours(current_route)
            city_1, city_2 = random.sample(range(self.__nr_cities), 2)
            cost_neighbour = self.__evaluate(neighbour)

            is_tabu = memory[city_1][city_2] > 0

            if not is_tabu and cost_neighbour < cost_current_route:
                current_route = neighbour
                cost_current_route = cost_neighbour

                memory[city_1][city_2] = self.__tabu_iterations

            for i in range(self.__nr_cities):
                for j in range(self.__nr_cities):
                    if memory[i][j] > 0:
                        memory[i][j] -= 1

        return cost_current_route

    #This method calculates the Euclidean distance between two cities. It takes 'city1' and 'city2' as parametres.
    #It extracts the x and y coordinates of the two cities and calculates and returns the Euclidean distance.
    def __get_city_distance(self, city1, city2):
        x1, y1 = self.__cities[city1]["city_x"], self.__cities[city1]["city_y"]
        x2, y2 = self.__cities[city2]["city_x"], self.__cities[city2]["city_y"]

        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    #This method generates neighboring solutions by reversing a random segment of the solution route.
    @staticmethod
    def generate_neighbours(solution):
        a, b = sorted(random.sample(range(len(solution)), 2))
        return solution[:a] + solution[a:b + 1][::-1] + solution[b + 1:]