

class TSP:
    def __init__(self, filename):
        self.__cities = []
        self.__nr_cities = 0

        self.__config_from_file(filename)

        def __config_from_file(self, filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.__number_of_cities = int(lines[0])

                lines = [line.strip() for line in lines if line.strip()]

                for line in lines[1:]:
                    parts = line.split()
                    city_id = int(parts[0])
                    city_x = int(parts[1])
                    city_y = int(parts[2])

                    self.__cities.append({"id": city_id, "city_x": city_x, "city_y": city_y})

