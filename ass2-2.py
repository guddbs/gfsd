import math

class Circle:
    PI = 3.14

    def __init__(self, x, y, radius):
        try:
            if radius <= 0:
                raise ValueError("반지름이 0보다 작거나 같습니다. 0보다 큰 반지름을 입력하세요.")
            self.__x = x
            self.__y = y
            self.__radius = radius
        except ValueError as e:
            print(e)

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def set_radius(self, radius):
        try:
            if radius <= 0:
                raise ValueError("반지름이 0보다 작거나 같습니다. 0보다 큰 반지름을 입력하세요.")
            self.__radius = radius
        except ValueError as e:
            print(e)

    def get_radius(self):
        return self.__radius

    def area(self):
        return round(self.PI * self.__radius**2, 2)

    def distance(self, c):
        return math.sqrt((self.__x - c.get_x())**2 + (self.__y - c.get_y())**2)

    def overlaps(self, c):
        return self.distance(c) < (self.__radius + c.get_radius())

    def contains(self, c):
        return self.distance(c) + c.get_radius() <= self.__radius

    def __str__(self):
        return f"Circle : (x={self.__x}, y={self.__y}, r={self.__radius}), 면적: {self.area()}"

# 인스턴스 생성 및 출력
c1 = Circle(0, 0, 100.2)
c2 = Circle(0, -10, 9.8)
c3 = Circle(-100, 0, 121.3)

print('c1 =', c1)
print('c2 =', c2)
print('c3 =', c3)
print('c1 contains c2:', c1.contains(c2))
print('c1 contains c3:', c1.contains(c3))
print('c1 overlaps c2:', c1.overlaps(c2))
print('c1 overlaps c3:', c1.overlaps(c3))