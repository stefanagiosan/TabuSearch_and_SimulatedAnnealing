import time

from search.tabu_search import TabuSearch
from write_file.tabu_search_write import TabuWrite


class UI:
    def __init__(self, filename):
        self.__k = 2000
        self.__tabu_iterations = 80
        self.__filename = filename
        self.__tabu_search = TabuSearch(filename)
        self.__exec = []
        self.__solutions = []

        self.__tabu_search_write = TabuWrite(filename, self.__k, self.__tabu_iterations)

    def menu(self):
        while True:
            print("1. Tabu Search")
            print("3. Iesire")

            choice = input("Dati optiunea: ")

            if choice == "1":
                self.__solutions = []
                self.__exec = []
                self.__tabu_search_write.info()

                for i in range(10):
                    start = time.time()
                    solution = self.__tabu_search.tabu_search(self.__k, self.__tabu_iterations)
                    end = time.time()
                    exec_time = end - start

                    self.__exec.append(exec_time)
                    self.__solutions.append(solution)
                    self.__tabu_search_write.write(solution, exec_time)

                self.__tabu_search_write.set_solutions(self.__solutions)
                self.__tabu_search_write.set_exec(self.__exec)
                self.__tabu_search_write.result()
            elif choice == "3":
                break
            else:
                print("Invalid Input")
