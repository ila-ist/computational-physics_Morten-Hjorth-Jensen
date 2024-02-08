class Vector:
    def __init__(self, elements):
        self.elements = elements

    def p_norm(self, p):
        return sum(abs(x)**p for x in self.elements)**(1/p)

    def inner_product(self, other):
        return sum(x.conjugate() * y for x, y in zip(self.elements, other.elements))

# check the Cauchy-Schwartz
def cauchy_schwartz(x, y):
    inner_prod = x.inner_product(y)
    norm_x = x.p_norm(2)  # Euclidean norm
    norm_y = y.p_norm(2)

    lhs = abs(inner_prod)
    rhs = norm_x * norm_y

    print(f"Left-hand side (|xT y|): {lhs}")
    print(f"Right-hand side (||x||2 * ||y||2): {rhs}")
    print(f"Is the inequality satisfied: {lhs <= rhs}")
    if lhs == rhs:
        print("x and y are linearly dependent.")

# Example usage:
x_values = [3, -4, 5]  # Replace with your vector elements
y_values = [1, 2, -1]  # Replace with your vector elements

x = Vector(x_values)
y = Vector(y_values)

# Calculate the p-norms
print(f"3-norm of x: {x.p_norm(3)}")
print(f"4-norm of y: {y.p_norm(4)}")

# Check Cauchy-Schwartz
print("\nChecking Cauchy-Schwartz inequality:")
cauchy_schwartz(x, y)
