class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_of_asphalt(self, asphalt_for_1m, thickness_of_asphalt):
        return f"{self.__length * self.__width * asphalt_for_1m * thickness_of_asphalt // 1000} т"


a = Road(20, 5000)
print(a.weight_of_asphalt(25, 5))
