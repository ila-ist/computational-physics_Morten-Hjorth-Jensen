class complex_var:
    def __init__(self, real, im):
        self.real = real
        self.im = im
        print('Real=', self.real, ' Image=', self.im, '\n')

    def add(self, other):
        print('\naddition')
        real = self.real + other.real
        im = self.im + other.im
        return complex_var(real, im)

    def sub(self, other):
        print('\nsubtraction')
        real = self.real - other.real
        im = self.im - other.im
        return complex_var(real, im)

    def mult(self, other):
        print('\nmultiplication')
        real = (self.real * other.real) - (self.im * other.im)
        im = (self.real * other.im) + (other.real * self.im)
        return complex_var(real, im)

    def div(self, other):
        print('\ndivision')
        r = (other.real ** 2 + other.im ** 2)
        real = ((self.real * (other.real)) + (self.im * other.im)) / r
        im = ((-1) * (self.real * other.im) + (other.real * self.im)) / r
        return complex_var(real, im)


z1 = complex_var(1, 2)
z2 = complex_var(3, 4)

z1.add(z2)
z1.sub(z2)
z1.mult(z2)
z1.div(z2)