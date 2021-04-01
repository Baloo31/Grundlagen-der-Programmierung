from Circle import Circle


class CircleBox:
    def __init__(self):
        self.List = []

    def add_circle(self, c):
        if isinstance(c, Circle):
            self.List.append(c)
        else:
            raise ValueError

    def print_circles(self):
        for circle in self.List:
            print(circle)

    def sort_circle(self):
        return sorted(self.List, reverse=True)
