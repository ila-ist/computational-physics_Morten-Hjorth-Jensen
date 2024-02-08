x = [1, 1.5, 10, 2.5]
y = [2, 3, 0, 70]
target_x = 1.75

n = len(x)
P = [[0] * n for _ in range(n)]
#print(P)

for i in range(n):
    P[i][0] = y[i]

print(P)

for i in range(1, n):
    print('i', i)
    for j in range(1, i + 1):
        print('           j', j)
        P[i][j] = ((target_x - x[i - j]) * P[i][j - 1] - (target_x - x[i]) * P[i - 1][j - 1]) / (x[i] - x[i - j])
        print('p', P)

#print(P)
print(P[n - 1][n - 1])