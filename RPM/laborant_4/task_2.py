class GeometricObject:
    pass

class Point(GeometricObject):
    pass

class Line(GeometricObject):
    pass

class FlatShape(GeometricObject):
    pass

class Ray(Point, Line):
    pass

class Segment(Point, Line):
    pass

class Polygon(FlatShape, Point):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass
