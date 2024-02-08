# نه چندان درست...

a = float(input("input 'a'"))
b = float(input("input 'b'"))
c = float(input("input 'c'"))
r = int(input("input 'r'")) #most significant lost bits
if (2 ** -r) <= 1 - (4 * a * c) / (b ** 2) and (2 ** -r) <= (4 * a * c) / (b ** 2):
    answer_1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    answer_2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    print("x_1 is", answer_1,"x_2 is", answer_2)
else:
    print("there is no answer")

