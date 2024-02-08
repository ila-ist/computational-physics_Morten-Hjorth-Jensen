class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(self.x, ',', self.y, ',', self.z, '\n')

    def add(self, other):
        print('\naddition')
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def dot(self, other):
        print('\ndot production')
        print(self.x.conjugate() * other.x + self.y.conjugate() * other.y + self.z.conjugate() * other.z)

    def mult(self, a):
        print('\nscalar production')
        return vector(self.x * a, self.y * a, self.z * a)


a = vector(1 - 1j, 2, 3)
b = vector(4 + 1j, 5, 6)

a.dot(b)
a.add(b)
a.mult(2)