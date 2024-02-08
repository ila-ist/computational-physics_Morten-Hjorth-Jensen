S = 1
x = abs(float(input())) # just x >= 0
l = []
for jomle in range(1, 20): # for x > 1
    l.append(S)
    #print(S)
    S = (S * x) / jomle #recursion relation for exp(x)
    if S < 1e-20: # for x < 1
        break

if x >= 1:
    exp_x = sum(l)

    print(l)
else:
    l.reverse()# we have to do sum from the smallest num
    exp_x = sum(l)

print(l)
print(sum(l))
exp_neg_x = 1 / exp_x
print(exp_neg_x)