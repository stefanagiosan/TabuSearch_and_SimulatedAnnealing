

class TabuWrite:
    def __init__(self, filename, k, it):
        self.__filename = filename
        self.__k = k
        self.__tabu_it = it
        self.__exec = []
        self.__solutions = []

    def set_exec(self, exec_time):
        self.__exec = exec_time

    def set_solutions(self, solutions):
        self.__solutions = solutions

    @staticmethod
    def write(solution, exec_time):
        with open("results/results_tabu.txt", "a") as file:
            file.write(f"{solution} <------> {exec_time}\n")

    def info(self):
        with open("results/results_tabu.txt", "a") as file:
            file.write(f"Se foloseste *Tabu Search* si se citesc datele din fisierul: {self.__filename}\n")
            file.write(f"Valoarea lui K = {self.__k} si numarul de executii este: 10\n")
            file.write(f"Iteratii Tabu: {self.__tabu_it}\n")

    def result(self):
        media_exec = sum(self.__exec) / len(self.__exec)
        media_solutions = sum(self.__solutions) / len(self.__solutions)
        max_solution = max(self.__solutions)

        with open("results/results_tabu.txt", "a") as file:
            file.write(f"Valoarea medie: {media_solutions}\n")
            file.write(f"Valoarea maxima: {max_solution}\n")
            file.write(f"Media timpului de executie: {media_exec}\n")