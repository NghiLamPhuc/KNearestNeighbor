'''
A Point has list of coordinate.

'''
class Point:
    def __init__(self, coordinit: list):
        self.coord = coordinit
        self.size = len(coordinit)
        
    def euclid_distance(self, secondPoint) -> float:
        d = 0
        for index in range(self.size):
            d += (self.coord[index] - secondPoint.coord[index])**2
        return d**0.5

    def cosine_distance(self, secondPoint) -> float:
        (sumxx, sumxy, sumyy) = (0, 0, 0)
        for i in range(self.size):
            x = self.coord[i]; y = secondPoint.coord[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy / ((sumxx * sumyy)**0.5)

    def display_with_parentheses(self) -> str:
        coordStr = ''
        for index in range(self.size - 1):
            coordStr += str(self.coord[index]) + ', '
        coordStr += str(self.coord[-1])
        return ''.join('(' + coordStr + ')')
    
    def display(self) -> str:
        coordStr = ''
        for index in range(self.size - 1):
            coordStr += str(self.coord[index]) + ', '
        coordStr += str(self.coord[-1])
        return ''.join(coordStr)

'''
P1 P2 P3 P4 ...
Finding a point by calculate average coordinate of all P.
'''
def calculate_midpoint_of_list(listPoints: list) -> list():
    midpoint = list()
    pointSize = listPoints[0].size
    for iCoord in range(pointSize):
        curr = 0
        for point in listPoints:
            curr += point.coord[iCoord]
        midpoint.append(curr/len(listPoints))
    return Point(midpoint)

'''
if two point is one -> 1
else                -> 0
'''
def compare_two_point(a: Point, b: Point) -> int:
    if a.size != b.size:
        return 0
    sumDifferent = 0
    for iCoordA in range(len(a.coord)):
        sumDifferent += a.coord[iCoordA] - b.coord[iCoordA]
    if sumDifferent == 0:
        return 0
    return 1

def testCompare():
    a = Point([1,2,3])
    b = Point([1,2,4])
    c = Point([1,2,3])
    print('a.[{0}]'.format(a.display()))
    print('b.[{0}]'.format(b.display()))
    print('c.[{0}]'.format(c.display()))
    if compare_two_point(a, c) == 0:
        print('a is c')
    if compare_two_point(a, b) == 1:
        print('a not b')

def main():
    testCompare()

if __name__=="__main__": main()
