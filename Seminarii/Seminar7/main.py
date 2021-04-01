from Point import Point
from Circle import Circle
from CircleBox import CircleBox


def main():
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(3, 4)
    c1 = Circle(p1, 5)
    c2 = Circle(p2, 4)
    """
    print(c1.compute_area())
    print(c2.compute_area())
    print(p1 + p2)
    print(c1 * c2)
    """
    cb = CircleBox()
    c3 = Circle(p3, 6)
    cb.add_circle(c1)
    cb.add_circle(c2)
    cb.add_circle(c3)
    cb.print_circles()
    print(cb.sort_circle())


main()
