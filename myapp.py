a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Điều kiện để a, b, c là độ dài ba cạnh của tam giác
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, c là độ dài 3 cạnh của một tam giác")
else:
    print("a, b, c KHÔNG phải là độ dài 3 cạnh của một tam giác")
