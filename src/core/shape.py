import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_dot_inside(self, x: float, y: float) -> bool:
        pass

    def change_color(self, color: str) -> None:
        self.color = color


class Rectangle(Shape):
    def __init__(
        self,
        x: tuple[float, float],
        y: tuple[float, float],
        fill_color: str = "None",
        draw_color: str = "black",
    ):
        self.x = x
        self.y = y
        self.fill_color = fill_color
        self.draw_color = draw_color

        self.xy = (min(self.x), min(self.y))
        self.width = max(self.x) - min(self.x)
        self.height = max(self.y) - min(self.y)

        self.coordinates = (self.xy, self.width, self.height)
        self.hitbox = ((min(x), max(x)), (min(y), max(y)))

    def is_dot_inside(self, x: float, y: float) -> bool:
        min_x = self.xy[0]
        max_x = min_x + self.width
        min_y = self.xy[1]
        max_y = min_y + self.height

        return min_x <= x <= max_x and min_y <= y <= max_y


class Ellipse(Shape):
    def __init__(
        self,
        x: tuple[float, float],
        y: tuple[float, float],
        fill_color: str = "None",
        draw_color: str = "black",
    ):
        self.x = x
        self.y = y
        self.fill_color = fill_color
        self.draw_color = draw_color

        self.x1 = (x[0] + x[1]) / 2
        self.y1 = (y[0] + y[1]) / 2
        self.width = x[1] - x[0]
        self.height = y[1] - y[0]

        self.coordinates = ((self.x1, self.y1), self.width, self.height)
        self.hitbox = ((min(x), max(x)), (min(y), max(y)))

    def is_dot_inside(self, x: float, y: float) -> bool:
        return (
            ((self.y1 - y) * (2 / self.height)) ** 2
            + ((self.x1 - x) * (2 / self.width)) ** 2
        ) <= 1


class Circle(Shape):
    def __init__(
        self,
        x: float,
        y: float,
        r: float,
        fill_color: str = "None",
        draw_color: str = "black",
    ):
        self.x = x
        self.y = y
        self.r = r
        self.fill_color = fill_color
        self.draw_color = draw_color

        self.coordinates = ((self.x, self.y), self.r)
        self.hitbox = ((x - r, x + r), (y - r, y + r))

    def is_dot_inside(self, x: float, y: float) -> bool:
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r**2


class Line(Shape):
    def __init__(
        self,
        x: tuple[float, float],
        y: tuple[float, float],
        draw_color: str = "black",
    ):
        self.x = x
        self.y = y
        self.draw_color = draw_color

        self.xy1 = (x[0], y[0])
        self.xy2 = (x[1], y[1])

        self.coordinates = (self.x, self.y)
        self.hitbox = ((min(x), max(x)), (min(y), max(y)))

    def is_dot_inside(self, x: float, y: float) -> bool:
        ret = 0
        ret += self.x[0] <= x <= self.x[1]
        ret += self.y[0] <= y <= self.y[1]

        k = (self.y[0] - self.y[1]) / (self.x[0] - self.x[1])
        b = self.y[0] - self.x[0] * k
        ret += y == k * x + b

        return bool(ret)
