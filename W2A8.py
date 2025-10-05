try:
    c = float(input("Nhập nhiệt độ °C: "))
    f = 9/5 * c + 32
    print(f"Độ °F: {f:.2f}")
except ValueError:
    print("Vui lòng nhập giá trị khác")