

class TabuWrite:
    def __init__(self, filename, k):
        self.filename = filename
        self.__k = k
        self.__exec = []
        self.__solutions = []

    def set_exec(self, exec):
        self.__exec = exec

    def set_solutions(self, solutions):
        self.__solutions = solutions

    @staticmethod
    def write(solution, exec):
        with open("results/result_tabu.txt", "a") as file:
            file.write(f"{solution} <------> {exec}\n")

    def info(self):
        with open("results/result_tabu.txt", "r") as file:
            file.write(f"Se foloseste *Tabu Search* si se citesc datele din fisierul: {self.__filename}\n")
            file.write(f"Valoarea lui K = {self.__k} si numarul de executii este: 10\n")

    def result(self):
        media_exec = sum(self.__exec) / len(self.__exec)
        media_solutions = sum(self.__solutions) / len(self)
        max_solution = max(self.__solutions)

        with open("results/result_tabu.txt", "w") as file:
            file.write(f"Valoarea medie: {media_exec}\n")
            file.write(f"Valoarea maxima: {max_solution}\n")
            file.write(f"Media timpului de executie: {media_exec}\n")