fuel = input("Fraction: ")
while True:
    try:
        x,y = fuel.split("/")
        t = int(x)
        w = int(y)
        f = t / w
        if f <= 1:
            break
    except (ValueError, ):
        pass
p = int(f*100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print (f"{p}%")

