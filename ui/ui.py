import time

from search.tabu_search import TabuSearch
from search.tsp import TSP
from write_file.write import OutputFileWriter


class UI:
    def __init__(self):
        self.__iterations = 0
        self.__tabu_iterations = 0

        self.__tabuSearch = None
        self.__tsp = None

        self.__execution_times = []
        self.__solutions = []

        self.__rucsac_file_writer = OutputFileWriter("data/rucsac.txt",
                                                     "results/results_tabu.txt", self.__iterations,
                                                     self.__tabu_iterations)
        self.__tsp_file_writer = OutputFileWriter("data/data.tsp", "results/results_tsp.txt",
                                                  self.__iterations, self.__tabu_iterations)

    def show_menu(self):
        while True:
            print("1. Problema rucsacului cu tabu search.")
            print("2. Problema comis-voiajorului cu tabu search.")
            print("x. Iesire")

            user_choice = input("Dati optiunea: ")

            if user_choice == "1":
                self.__iterations = int(input("Dati numarul de iteratii: "))
                self.__tabu_iterations = int(input("Dati numerul de iteratii tabu: "))

                self.__tabuSearch = TabuSearch("data/rucsac.txt",
                                               self.__iterations, self.__tabu_iterations)

                self.__solutions = []
                self.__execution_times = []

                self.__rucsac_file_writer.initial_write_file()

                for i in range(10):
                    start_time = time.time()
                    solution = self.__tabuSearch.search()
                    end_time = time.time()
                    execution_time = end_time - start_time

                    self.__solutions.append(solution)
                    self.__execution_times.append(execution_time)
                    self.__rucsac_file_writer.write_file(solution, execution_time)

                self.__rucsac_file_writer.set_solutions(self.__solutions)
                self.__rucsac_file_writer.set_execution_times(self.__execution_times)
                self.__rucsac_file_writer.final_write_file()

                print("Datele au fost procesate.")
            elif user_choice == "2":
                self.__iterations = int(input("Dati numarul de iteratii: "))
                self.__tabu_iterations = int(input("Dati numerul de iteratii tabu: "))

                self.__tsp = TSP("data/data.tsp", self.__iterations,
                                 self.__tabu_iterations)

                self.__solutions = []
                self.__execution_times = []

                self.__tsp_file_writer.initial_write_file()

                for i in range(10):
                    start_time = time.time()
                    solution = self.__tsp.search()
                    end_time = time.time()
                    execution_time = end_time - start_time

                    self.__solutions.append(solution)
                    self.__execution_times.append(execution_time)
                    self.__tsp_file_writer.write_file(solution, execution_time)

                self.__tsp_file_writer.set_solutions(self.__solutions)
                self.__tsp_file_writer.set_execution_times(self.__execution_times)
                self.__tsp_file_writer.final_write_file()

                print("Datele au fost procesate.")
            elif user_choice == "x":
                break
            else:
                print("Optiune Invalida.")
