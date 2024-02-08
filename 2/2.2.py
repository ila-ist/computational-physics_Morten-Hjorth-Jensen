sum  = 0
n = 10 ** 5
c = 0
for i in range(1, n):
    x = 1 / i
    sum += x
    c += 1
    print(c)

print("{:.52f}".format(sum))


l_reversed = []
l = [j for j in range(1, n)]
for num in range(1, n):
    l_reversed.append(l[-1])  # tamame inha ro mishod ba ye method anjam dad
    del l[-1]


sum_reversed = 0
for m in l_reversed:
    y = 1 / m
    sum_reversed += y

print("{:.52f}".format(sum_reversed))# javab vaqei ro be dast biaram...
