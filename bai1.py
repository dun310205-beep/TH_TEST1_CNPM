def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

print("Bội chung nhỏ nhất của", a, "và", b, "là:", lcm(a, b))
