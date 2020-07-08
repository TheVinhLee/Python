# demonstrate override the object operator

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x: {0}, y:{1}>".format(self.x, self.y)

    '''
    goal is to be unambiguous
    '''

    # TODO: implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    '''
    normally cannot add two classes
    '''

    # TODO: implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    '''
    used to subtract 2 classes
    '''

    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: Add two points
    p3 = p1 + p2
    print(p3)

    # TODO: subtract two points
    p4 = p1 - p2
    print(p4)

    # TODO: Perform in-place addition
    p1 += p2
    '''
    normally will have None result, need in-place to solved it
    '''
    print(p1)


if __name__ == '__main__':
    main()