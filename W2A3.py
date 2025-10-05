a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b
phan_nguyen = a // b
phan_du = a % b
chia_thuc = round(a / b, 2)

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Phần nguyên:", phan_nguyen)
print("Phần dư:", phan_du)
print("Chia thực (lấy 2 chữ số thập phân):", chia_thuc)