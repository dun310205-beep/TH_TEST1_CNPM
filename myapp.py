a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tạo thành tam giác
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, c là ba cạnh của một tam giác")

    # Kiểm tra tam giác đều
    if a == b == c:
        print("→ Đây là tam giác đều")

    # Kiểm tra tam giác cân
    elif a == b or a == c or b == c:

        # Kiểm tra tam giác vuông cân
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            print("→ Đây là tam giác vuông cân")
        else:
            print("→ Đây là tam giác cân")

    else:
        # Kiểm tra tam giác vuông
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            print("→ Đây là tam giác vuông")

        # Kiểm tra tam giác tù
        elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (b*b + c*c < a*a):
            print("→ Đây là tam giác tù")

        # Còn lại là tam giác nhọn
        else:
            print("Đây là tam giác nhọn")

else:
    print("a, b, c KHÔNG phải là ba cạnh của một tam giác")
