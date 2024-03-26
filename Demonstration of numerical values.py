a = int(input("Enter the numeric value: "))

t = a / 2000
t1 = int(t)
t2 = str(t1)
t3 = (a - (2000 * t1))

f =  t3 / 500
f1 = int(f)
f2 = str(f1)
f3 = (t3 - (500 * f1))

tw = f3 / 200
tw1 = int(tw)
tw2 = str(tw1)
tw3 = (f3 - (200 * tw1))

o = tw3 / 100
o1 = int(o)
o2 = str(o1)

print("2000: " + t2 + " 500: " + f2 + " 200: " + tw2 + " 100: " + o2) 