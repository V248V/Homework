from math import sqrt

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides
        if isinstance(color, tuple) and len(color) == 3:
            self.__color = color
        else:
            print("The color is not right. Set to be (255, 255, 255)")
            self.__color = (255, 255, 255)
        self.filled = True
        self._Figure__testing_func()


    def get_color(self):
        return self.__color

    def __is_valid_color(self, red, green, blue):
        if red >= 0 and red <= 255:
            if green >= 0 and green <= 255:
                if blue >= 0 and blue <= 255:
                    return True

    def set_color(self, red, green, blue):
        if Figure.__is_valid_color(self, red, green, blue):
            self.__color = (red, green, blue)

    def __is_valid_sides(self, *sides):
        if len(sides) == len(self.__sides):
            if all(isinstance(x, int) for x in sides):
                if all(j >= 1 for j in sides):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def get_sides(self):
        return self.__sides

    def __len__(self):
        perim = 0
        for i in self.__sides:
            perim += i
        return perim

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            pass

    def __testing_func(self):
        __test_list = []
        if len(self._Figure__sides) == self.sides_given:
            for i in range(0, self.sides_count):
                __test_list.append(self._Figure__sides[0])
            self._Figure__sides = tuple(__test_list)
        else:
            for i in range(0, self.sides_count):
                __test_list.append(1)
            self._Figure__sides = tuple(__test_list)

class Circle(Figure):
    sides_count = 1
    sides_given = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__radius = sides[0] / 6.28
        else:
            self.__radius = 1 / 6.28

    def get_square(self):
        square_of_circle = 3.14 * self.__radius**2
        return square_of_circle


class Triangle(Figure):
    sides_count = 3
    sides_given = 3

    def get_square(self):
        p_per = self.__len__() / 2
        square_of_triangle = sqrt(p_per * (p_per - self._Figure__sides[0]) *
                                 (p_per - self._Figure__sides[1]) * (p_per - self._Figure__sides[2]))
        return square_of_triangle


class Cube(Figure):
    sides_count = 12
    sides_given = 1

    def get_volume(self):
        cube_volume = self._Figure__sides[0]**3
        return cube_volume






circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
