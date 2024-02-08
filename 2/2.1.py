num = float(input())
#int_fl = str(num % 1) # kharab...
i, f = int(num), num*1e17%1e17/1e17

l_f = []
coun = 0
while True: # برای قسمت اعشاری
    coun += 1
    f = f * 2
    if f >= 1:
        f = f - 1
        l_f.append(str(1))
    elif 0 < f and f < 1:
        l_f.append(str(0))
    else:
        break

    if coun == 20:# baraye adadi ke bar migirand
        break
    #print(f)

fl = ''.join(l_f)

# حالا قسمت صحیح
x = i // 2
l_baqi = []
while i >= 2:
    #print("baqi", num%2)
    #print(x)
    l_baqi.append(str(i % 2))
    #print(l_baqi)
    i = x
    x = i // 2    #خارج قسمت

l_baqi.reverse()
#print(l_baqi)
baqiha = ''.join(l_baqi)
#print(baqiha)
kharej_q = str(i)



print(kharej_q, baqiha,'.', fl, sep='')# fasele...
