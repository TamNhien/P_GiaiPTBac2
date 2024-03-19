import math

a, b, c = map(float, input("Nhập hệ số a, b, c: ").split())

if a == 0:
    if b == 0:
        print("PTVN" if c != 0 else "PT có VSN")
    else:
        x1 = x2 = -c / b
        print("PT có nghiệm x = ", x1)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("PTVN")
    elif delta == 0:
        x1 = x2 = -b / (2 * a)
        print("PT có nghiệm kép x1 = x2 = ", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("PT có 2 nghiệm phân biệt : ")
        print("x1 = ", x1)
        print("x2 = ", x2)

